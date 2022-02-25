class User():
    """making a user profile"""

    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def describe_user(self):
        print(f"The name of the user is:")
        print(f"{self.first.title()} {self.last.title()}")

    def greet_user(self):
        print(f"Hello {self.first.title()} {self.last.title()}!")


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


class Admin(User):
    """Making an admin user."""

    def __init__(self, first_name, last_name):
        """Initializing inheritance."""
        super().__init__(first_name, last_name)

        self.privileges = Privileges()
        # making the class Privileges an attribute

    def message(self):
        """Defining message to Admin."""
        print(f"As {self.first.title()}, you are authorized to:")


admin_0 = Admin('Admin', '')
admin_0.message()

list_privileges = ['add post', 'delete post', 'ban user', 'give privileges']

admin_0.privileges.modify_privileges(list_privileges)
admin_0.privileges.show_privileges()
# admin_0.privilege.show_privileges()
# admin_privileges.show_privileges(list_privileges)
# 1. list at the end
# 2. make a variable for the class and if inheritance:
# add parameters in parenthesis
# 3. variable from point 2, method you want to call and
# within parenthesis the variable that contains the arguments/values
