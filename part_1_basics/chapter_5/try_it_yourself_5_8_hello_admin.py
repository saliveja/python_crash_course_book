# making a list with users and printing a greeting to each of them
users = ['admin', 'tor', 'greta', 'linnea', 'ben']
for user in users:
    if user == 'admin':
        # if the user is 'admin'
        # printing --> 'Hello admin, there is no new updates on the project'
        print("Hello " + user.title() + ", there is no new updates on the"
                                        " project.")
    else:
        print("Hello " + user.title() + ", and welcome!")
        # for all other users 'Hello user, and welcome! is printed
