users = ['admin', 'tor', 'greta', 'linnea', 'ben']
for user in users:
    if user == 'admin':
        print("Hello " + user.title() + ", there is no new updates on the"
                                        " project.")
    else:
        print("Hello " + user.title() + ", and welcome!")
# making a list with users and printing a greeting to each of them
# for the user admin a special greeting will be printed
