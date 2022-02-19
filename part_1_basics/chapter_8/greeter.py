# defining a function
def greet_user():
    # defining the function
    """Display a simple greeting."""
    # using tripple quotation with text is called a docstring
    # the tripple quotation is known to python
    print("Hello!")
    # anything after colon is the body of the function


greet_user()

# to call a function we write the name of the function
# any other necessary info is added in the parenthesis

# passing information to a function
users = ['anna', 'jesse', 'can']


def greet_user(user):
    """Display a simple greeting."""
    print(f"Hello, {user.title()}!")


greet_user('jesse')
# making a list with three names
# defining a function
# the variable within the parenthesis is a parameter,
# information needed for the function to do it's job
# 'jesse' is a value and an argument
# passed from a function to call a function

for user in users:
    greet_user(user)
    # making a for loop
    # calling for the function for the list
