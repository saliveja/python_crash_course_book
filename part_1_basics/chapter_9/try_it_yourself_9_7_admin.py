class User():
    """making a user profile"""

    def __init__(
            self, first_name, last_name
    ):
        self.first = first_name
        self.last = last_name

    def describe_user(self):
        print(f"The name of the user is:")
        print(f"{self.first.title()} {self.last.title()}")

    def greet_user(self):
        print(f"Hello {self.first.title()} {self.last.title()}!")


class Admin(User):
    """Making an admin user."""

    def __init__(
            self, first_name, last_name
    ):
        super().__init__(first_name, last_name)
        self.privileges = privileges
        privileges = ['can add post', 'can delete post', 'can ban user',
                      'can give privileges']

def show_privileges(self, privileges):
