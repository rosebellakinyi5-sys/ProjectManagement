from models.person import Person

class User(Person):
  """Represents a User system entity, inheriting from Person."""
  _id_counter = 1 # Class attribute for tracking auto-increment IDs

def __init__(self, name: str, email: str, user_id: int = None):
  super().__init__(name)
  self._email = email
  if user_id is not None:
    self.id = user_id
    if user_id >= User._id_counter:
        User._id_counter = user_id + 1
  else:
   self.id = User._id_counter
   User._id_counter += 1

@property
def email(self) -> str:
  """Gets the user's email address."""
  return self._email

@email.setter
def email(self, value: str):
   """Validates and sets the email address."""
   if "@" not in value or "." not in value:
    raise ValueError("Invalid email formatting standard.")
   self._email = value.strip()

def to_dict(self) -> dict:
   """Serializes user info to dictionary."""
   return {"id": self.id, "name": self.name, "email": self.email}

def __str__(self) -> str:
   return f"[User ID {self.id}] {self.name} ({self.email})"