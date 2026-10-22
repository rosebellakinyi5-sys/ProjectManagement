import os
import json

from psutil import users
from models.user import User
from models.project import Project
from models.task import Task

DATA_FILE = os.path.join("data", "storage.json")

def load_data():
    """Loads records from the JSON database safely, recovering from malformed states."""
    default_schema = {"users": [], "projects": [], "tasks": []}

    if not os.path.exists(DATA_FILE):
     return default_schema

    try:
     with open(DATA_FILE, "r") as f:
       return json.load(f)
    except (json.JSONDecodeError, IOError):
         
# Graceful error management & fallback recovery
      return default_schema

def save_data(data: dict):
   """Saves records safely down into the local JSON data store file."""
   if not os.path.exists("data"):
    os.makedirs("data")
    with open(DATA_FILE, "w") as f:
     json.dump(data, f, indent=4)

def get_all_objects():
   """Initializes models directly using structured data arrays loaded from storage."""
   raw = load_data()
   users = [User(u["name"], u["email"], u["id"]) for u in raw.get("users", [])]
   projects = [Project(p["title"], p["description"], p["due_date"], p["user_id"], p["id"]) for p in raw.get("projects", [])]
   tasks = [Task(t["title"], t["project_id"], t["assigned_to"], t["status"], t["id"]) for t in raw.get("tasks", [])]
   return users, projects, tasks

def save_all_objects(users, projects, tasks):
   """Packages object arrays into dictionaries and saves them to disk."""
   payload = {
      "users": [u.to_dict() for u in users],
      "projects": [p.to_dict() for p in projects],
      "tasks": [t.to_dict() for t in tasks]
   }
   save_data(payload)