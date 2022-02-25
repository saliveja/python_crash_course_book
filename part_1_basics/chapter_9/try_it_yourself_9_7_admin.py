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


class Admin(User):
    """Making an admin user."""

    def __init__(self, first_name, last_name):
        """Initializing inheritance."""
        super().__init__(first_name, last_name)

    def show_privileges(self, privileges):
        self.privileges = privileges
        print(f"As {self.first.title()}, you are authorized to:")
        for privilege in self.privileges:
            print(privilege)


list_privileges = ['can add post', 'can delete post', 'can ban user',
                   'can give privileges']

admin_privileges = Admin('Admin', '')
admin_privileges.show_privileges(list_privileges)
# 1. list at the end
# 2. make a variable for the class and if inheritance:
# add parameters in parenthesis
# 3. variable from point 2, method you want to call and
# within parenthesis the variable that contains the arguments/values
