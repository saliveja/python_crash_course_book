def magician_list(names):
    """printing names of magicians"""
    for name in names:
        info = f"{name.title()}"
        print(info)


show_magicians = ['fyr', 'leo', 'kyro', 'seth']
magician_list(show_magicians)
# using for loop in a function to print each name in the list of magicians
