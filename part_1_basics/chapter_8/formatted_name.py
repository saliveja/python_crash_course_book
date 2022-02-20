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
