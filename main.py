import argparse
from rich.console import Console
from rich.table import Table
from utils.storage_handler import get_all_objects, save_all_objects
from models.user import User
from models.project import Project
from models.task import Task

console = Console()


def handle_add_user(args):
    users, projects, tasks = get_all_objects()
    if any(u.name.lower() == args.name.lower() for u in users):
        console.print(f"[bold red]Error:[/bold red] A user named '{args.name}' already exists.")
        return

    try:
        new_user = User(name=args.name, email=args.email)
        users.append(new_user)
        save_all_objects(users, projects, tasks)
        console.print(f"[bold green]Success:[/bold green] Created user {new_user}")
    except ValueError as e:
        console.print(f"[bold red]Validation Error:[/bold red] {e}")


def handle_add_project(args):
    users, projects, tasks = get_all_objects()
    target_user = next((u for u in users if u.name.lower() == args.user.lower()), None)

    if not target_user:
        console.print(f"[bold red]Error:[/bold red] User target '{args.user}' not found.")
        return

    try:
        new_project = Project(
            title=args.title,
            description=args.desc,
            due_date=args.due,
            user_id=target_user.id,
        )
        projects.append(new_project)
        save_all_objects(users, projects, tasks)
        console.print(
            f"[bold green]Success:[/bold green] Created project {new_project} for user {target_user.name}"
        )
    except ValueError as e:
        console.print(f"[bold red]Validation Error:[/bold red] {e}")


def handle_add_task(args):
    users, projects, tasks = get_all_objects()
    target_project = next((p for p in projects if p.title.lower() == args.project.lower()), None)

    if not target_project:
        console.print(f"[bold red]Error:[/bold red] Project target '{args.project}' not found.")
        return

    try:
        new_task = Task(
            title=args.title,
            project_id=target_project.id,
            assigned_to=args.assignee,
        )
        tasks.append(new_task)
        save_all_objects(users, projects, tasks)
        console.print(
            f"[bold green]Success:[/bold green] Added task '{new_task.title}' to project '{target_project.title}'"
        )
    except ValueError as e:
        console.print(f"[bold red]Validation Error:[/bold red] {e}")


def handle_list_projects(args):
    users, projects, tasks = get_all_objects()

    table = Table(title="Project Management Dashboard")
    table.add_column("User Owner", style="cyan")
    table.add_column("Project Name (ID)", style="magenta")
    table.add_column("Due Date", style="green")
    table.add_column("Tasks Remaining / Total", style="yellow")

    for u in users:
        user_projects = [p for p in projects if p.user_id == u.id]
        for p in user_projects:
            proj_tasks = [t for t in tasks if t.project_id == p.id]
            pending_count = len([t for t in proj_tasks if t.status != "Complete"])
            table.add_row(
                u.name,
                f"{p.title} (#{p.id})",
                str(p.due_date),
                f"{pending_count}/{len(proj_tasks)}",
            )

            # Sub-tasks printed directly under their project
            for t in proj_tasks:
                status_color = "green" if t.status == "Complete" else "red"
                table.add_row(
                    "",
                    f" ↳ [{status_color}]{t.status[:4]}[/{status_color}] {t.title}",
                    f"Assigned: {t.assigned_to}",
                    "",
                )

    console.print(table)


def handle_complete_task(args):
    users, projects, tasks = get_all_objects()
    task_to_update = next((t for t in tasks if t.id == args.task_id), None)

    if not task_to_update:
        console.print(f"[bold red]Error:[/bold red] Task with explicit ID {args.task_id} could not be matched.")
        return

    task_to_update.status = "Complete"
    save_all_objects(users, projects, tasks)
    console.print(f"[bold green]Success:[/bold green] Task {task_to_update.id} updated successfully to Complete.")


def main():
    parser = argparse.ArgumentParser(description="Multi-User Command-Line Project Tracking Infrastructure Toolkit")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add-user
    u_parser = subparsers.add_parser("add-user", help="Register a brand new developer profile.")
    u_parser.add_argument("--name", required=True, help="Developer's unique name.")
    u_parser.add_argument("--email", default="developer@company.local", help="Developer's email address.")
    u_parser.set_defaults(func=handle_add_user)

    # add-project
    p_parser = subparsers.add_parser("add-project", help="Create a project tied to a user.")
    p_parser.add_argument("--user", required=True, help="Username of the project owner.")
    p_parser.add_argument("--title", required=True, help="Project title.")
    p_parser.add_argument("--desc", default="No description provided", help="Project description.")
    p_parser.add_argument("--due", default="2026-12-31", help="Due date (YYYY-MM-DD).")
    p_parser.set_defaults(func=handle_add_project)

    # add-task
    t_parser = subparsers.add_parser("add-task", help="Add a task to a project.")
    t_parser.add_argument("--project", required=True, help="Exact name of the parent project.")
    t_parser.add_argument("--title", required=True, help="Task title.")
    t_parser.add_argument("--assignee", default="Unassigned", help="Name of the person responsible.")
    t_parser.set_defaults(func=handle_add_task)

    # list-projects
    l_parser = subparsers.add_parser("list-projects", help="Show all projects and their tasks.")
    l_parser.set_defaults(func=handle_list_projects)

    # complete-task
    c_parser = subparsers.add_parser("complete-task", help="Mark a task as complete.")
    c_parser.add_argument("--task-id", type=int, required=True, help="Numeric ID of the task.")
    c_parser.set_defaults(func=handle_complete_task)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()