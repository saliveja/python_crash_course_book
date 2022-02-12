users = ['admin', 'tor', 'greta', 'linnea', 'ben']
if users:
    for user in users:
        if user == 'admin':
            # if the user in the list is called 'admin'
            print("Hello " + user.title() + ", there is no new updates.")
            # printing 'hello admin, there is no updates'
        else:
            print("Welcome " + user.title() + "!")
            # for any other user printing 'Welcome user!'
else:
    print("We need to find some users!")
    # else on line 8 is outside of the loop
    # this code runs only if the first if statement "if users" falls:
    # if the list is empty

print("\n\n")
users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user.title() + ", there is no new updates.")
        else:
            print("Welcome " + user.title() + "!")
else:
    print("We need to find some users!")
    # this list is empty --> printing 'We need to find some user!'

