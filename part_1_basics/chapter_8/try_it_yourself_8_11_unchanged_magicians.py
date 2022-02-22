def make_great(magicians_old, magicians_new):
    # the parameters can be any name
    # therefore, we want them to be as decriptive as possible,
    # so the code is easy to read
    """making copy of list"""

    while magicians_old:
        current_magician = magicians_old.pop()
        # the variable defines current magician as the old
        # using pop to remove from the list
        # we are using pop with the !parameter!
        magicians_new.append(current_magician)
        # again using the parameter when appending current magician
        print(f"Copying {current_magician.title()} into the new list.")


magicians = ['fyr', 'leo', 'kyro', 'seth']
# list of old magicians
magicians_copy = []
# list of new magicians

print("\n")
make_great(magicians[:], magicians_copy)
# make sure to put the names of list when calling the function
# we use positional argument and magicians[:} equals magicians_old
# magicians_copy equals magicians_new

print(magicians)
# printing the original list
print(magicians_copy)
# printing the copy
