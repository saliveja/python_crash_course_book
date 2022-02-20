# returning a simple value
def get_formatted_name(first_name, last_name):
    # defining function, including parameters
    """Return a full name neatly formatted"""
    full_name = (f"{first_name} {last_name}")
    # making variable that combines the two parameters
    return full_name.title()
    # returning full name starting with upper case letter


musician = get_formatted_name('jimi', 'hendrix')
# creating a variable which equals calling the function and including values
print(musician)


# making an argument optional
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = (f"{first_name} {middle_name} {last_name}")
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

print("\n\n")


# making an argument optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        # if the middle name is included in the function call
        # the condition is met and the full name will be printed
        full_name = (f"{first_name} {middle_name} {last_name}")
    else:
        full_name = (f"{first_name} {last_name}")
        # if not, the first and the last name will be printed
    return full_name.title()


musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
