# try it yourself 9-7 and 9-8 together

class User():
    """making a user profile"""

    # parent class inherited in class Admin

    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def describe_user(self):
        print(f"The name of the user is:")
        print(f"{self.first.title()} {self.last.title()}")
        # we don't call this method

    def greet_user(self):
        print(f"Hello {self.first.title()} {self.last.title()}!")
        # we don't call this method


class Privileges():
    """Defining admin privileges."""

    def __init__(self, privileges=[]):
        """Listing privileges for user."""
        self.privileges = privileges
        # adding privileges to parameters
        # defining value as empty

    def modify_privileges(self, modified_privileges):
        """Modify the list of privileges"""
        self.privileges = modified_privileges
        # this method is the list the admin is authorized to do

    def show_privileges(self):
        """Displays the privileges"""
        for item in self.privileges:
            print(item)
            # this method loops through the list


class Admin(User):
    """Making an admin user."""

    def __init__(self, first_name, last_name):
        """Initializing inheritance."""
        super().__init__(first_name, last_name)
        # this class inherited from the class User

        self.privileges = Privileges()
        # making the class Privileges an attribute

    def message(self):
        """Defining message to Admin."""
        print(f"As {self.first.title()}, you are authorized to:")
        # this method is printing an initial message to admin,
        # before printing the list


admin_0 = Admin('Admin', '')
# 2. making the class Admin into a variable and arguments to 'Admin' and ''
admin_0.message()
# calling method message

list_privileges = ['add post', 'delete post', 'ban user', 'give privileges']
# 1. The list we want to print

admin_0.privileges.modify_privileges(list_privileges)
# 3. variable for Admin class, Privilege class and calling the list
# through method modify_list
admin_0.privileges.show_privileges()
# admin_0.privilege.show_privileges()
# 1. list at the end
# 2. make a variable for the class and if inheritance:
# add parameters in parenthesis
# 3. variable from point 2, another class you refer to -- int his case
# 'privileges' and/or method you want to call & within parenthesis the
# variable that contains the arguments/values
# here we have one method for the list and one for printing the list
