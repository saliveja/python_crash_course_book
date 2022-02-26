class Privileges():
    """Defining admin privileges."""

    def __init__(self, privileges=[]):
        """Listing privileges for user."""
        self.privileges = privileges

    def modify_privileges(self, modified_privileges):
        """Modify the list of privileges"""
        self.privileges = modified_privileges

    def show_privileges(self):
        """Displays the privileges"""
        for item in self.privileges:
            print(item)


from user_9_12 import User


class Admin(User):
    """Making an admin user."""

    def __init__(self, first_name, last_name):
        """Initializing inheritance."""
        super().__init__(first_name, last_name)

        self.privileges = Privileges()

    def message(self):
        """Defining message to Admin."""
        print(f"As {self.first.title()}, you are authorized to:")


list_privileges = ['add post', 'delete post', 'ban user',
                   'give privileges']
