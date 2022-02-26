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
