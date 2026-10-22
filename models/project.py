class Project:
  """Represents a discrete project owned by a single user."""
  _id_counter = 1

def __init__(self, title: str, description: str, due_date: str, user_id: int, project_id: int = None):
  self._title = title
  self.description = description
  self.due_date = due_date
  self.user_id = user_id

  if project_id is not None:
   self.id = project_id
  if project_id >= Project._id_counter:
   Project._id_counter = project_id + 1
  else:
   self.id = Project._id_counter
Project._id_counter += 1

@property
def title(self) -> str:
  """Gets the project title."""
  return self._title

@title.setter
def title(self, value: str):
    """Sets the project title with validation."""
    if not value or not value.strip():
        raise ValueError("Project title cannot be empty.")
    self._title = value.strip()

def to_dict(self) -> dict:
    """Serializes project info to dictionary."""
    return {
"id": self.id,
"title": self.title,
"description": self.description,
"due_date": self.due_date,
"user_id": self.user_id
}