class Privileges():
    """jhgfduihfguhifguhi"""

    def __init__(self, privileges):
        """Listing privileges for user."""
        privileges = []
        self.privileges = privileges

    def show_privileges(self, privileges):
        self.privileges = privileges
        print(f"As {self.first.title()}, you are authorized to:")
        for privilege in self.privileges:
            print(privilege)


