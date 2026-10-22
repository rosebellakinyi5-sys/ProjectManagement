class Task:
    """Represents an actionable task belonging to a specific project."""
    _id_counter = 1

def __init__(self, title: str, project_id: int, assigned_to: str = "Unassigned", status: str = "Pending", task_id: int = None):
    self._title = title
    self.project_id = project_id
    self.assigned_to = assigned_to
    self.status = status

    if task_id is not None:
     self.id = task_id
    if task_id >= Task._id_counter:
        Task._id_counter = task_id + 1
    else:
        self.id = Task._id_counter
Task._id_counter += 1

@property
def title(self) -> str:
    """Gets the task title."""
    return self._title

@title.setter
def title(self, value: str):
    """Sets and validates the task title."""
    if not value or not value.strip():
        raise ValueError("Task title cannot be empty.")
    self._title = value.strip()

def to_dict(self) -> dict:
    """Serializes task data to a dictionary payload."""
    return {
"id": self.id,
"title": self.title,
"project_id": self.project_id,
"assigned_to": self.assigned_to,
"status": self.status
}

def __str__(self) -> str:
    status_marker = "✓" if self.status == "Complete" else "⬪"
    return f" [{status_marker}] Task {self.id}: {self.title} (Assigned to: {self.assigned_to})"
