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


# using a function with a while loop
def get_formatted_name(first_name, last_name):
    # in this exercise, the parameters are not defined
    # there will be an input which will create the value
    """Return full name, neatly formatted."""
    full_name = (f"{first_name} {last_name}")
    return full_name.title()
    # it is defined how the name will be returned


while True:
    print("\nPlease tell me your name:")
    print("(enter q at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    # here we are using the values from the input
    print(f"\nHello, {formatted_name}!")
    # and printing them in this sentence
