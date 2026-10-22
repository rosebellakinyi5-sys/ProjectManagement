class Person:
    """Represents a base person with standard identification attributes."""

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        """Returns the name of the person."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Sets the name of the person."""
        if not value or not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value.strip()