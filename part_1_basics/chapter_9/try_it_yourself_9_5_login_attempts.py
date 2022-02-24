class User():
    """making a user profile"""

    def __init__(
            self, first_name, last_name,
    ):
        # __init__ including two parameters, first name and last name
        self.first = first_name
        self.last = last_name
        self.login_attempts = 0
        # the default value for login_attempts is set to zero

    def describe_user(self):
        print(f"The name of the user is:")
        print(f"{self.first.title()} {self.last.title()}")
        # making a method that prints the name of the user

    def greet_user(self):
        print(f"Hello {self.first.title()} {self.last.title()}!")
        print("\n")
        # method that prints a greeting to the user
        # including first and last name

    def increment_login_attempt(self, number):
        self.login_attempts += number
        # method to compund number of login attempts

    def login_message(self):
        print(f"{self.first.title()} {self.last.title()} tried to "
              f"login {self.login_attempts} times.")
        # method printing a message of how many times
        # a user tried to login


user_1 = User('kenny', 'svensson')
user_1.describe_user()
# info about user
user_1.greet_user()
# greeting to user
user_1.increment_login_attempt(8)
# adding number of login attempts
user_1.increment_login_attempt(5)
# adding number of login attempts
user_1.login_message()
# printing message about the login attempts

print("\n")

user_2 = User('solveig', 'andersson')
user_2.describe_user()
user_2.greet_user()
user_2.increment_login_attempt(13)
user_2.login_message()

print("\n")

user_3 = User('cathryn', 'sol')
user_3.describe_user()
user_3.greet_user()
user_3.increment_login_attempt(4)
user_3.login_message()
user_3.increment_login_attempt(9)
user_3.login_message()
