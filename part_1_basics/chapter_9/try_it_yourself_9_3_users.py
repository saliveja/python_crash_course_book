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


user_1 = User('kenny', 'svensson')
user_1.describe_user()
user_1.greet_user()

print("\n")

user_2 = User('solveig', 'andersson')
user_2.describe_user()
user_2.greet_user()

print("\n")

user_3 = User('cathryn', 'sol')
user_3.describe_user()
user_3.greet_user()
