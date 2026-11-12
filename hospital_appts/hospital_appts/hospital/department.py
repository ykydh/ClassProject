class Department:
    def __init__(self, department_id: str, name: str):
        # Using a single leading underscore indicates a protected/private attribute
        self._department_id = department_id
        self._name = name

    @property
    def department_id(self) -> str:
        """Getter for department ID."""
        return self._department_id

    @property
    def name(self) -> str:
        """Getter for department name."""
        return self._name