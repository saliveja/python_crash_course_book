def magician_list(names):
    """printing names of magicians with text"""
    for name in names:
        info = f"The great {name.title()}!"
        # adding the text to the variable in for loop
        print(info)


show_magicians = ['fyr', 'leo', 'kyro', 'seth']
magician_list(show_magicians)
