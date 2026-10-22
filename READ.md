# Python Project Management CLI Tool

A lightweight, modular **command-line application** built with Python 3.10+ to track multi-user projects and tasks. The system manages relational data models locally using structured JSON file persistence.

## 🚀 Features

* **User Profiles:** Provision and track individual team members.
* **Project Tracking:** Map projects to specific user owners (One-to-Many).
* **Task Management:** Assign actionable tasks to projects with status tracking.
* **Local Persistence:** Automated save/load operations utilizing file I/O operations (`storage.json`).
* **Modular Architecture:** Fully structured using object-oriented classes and modular components.

## 🛠️ Installation

1. **Verify Python Version:** Ensure you have Python 3.10 or higher installed.
2. **Install Dependencies:** Setup external formatting or input validation packages using pip:
```bash
pip install -r requirements.txt
```

## 💻 Usage Guide

Follow this sequence to cleanly provision your database and map data associations:

### 1. Add a User
```bash
python main.py add-user --name "Alex" --email "alex@domain.com"
```

### 2. Create a Project
```bash
python main.py add-project --user "Alex" --title "CLI Tool" --desc "Build Python application"
```

### 3. Add a Task
```bash
python main.py add-task --project "CLI Tool" --title "Implement add-task" --assignee "Alex"
```

### 4. List Projects & Statuses
```bash
python main.py list-projects
```

### 5. Complete a Task
```bash
python main.py complete-task --task-id 1
```
