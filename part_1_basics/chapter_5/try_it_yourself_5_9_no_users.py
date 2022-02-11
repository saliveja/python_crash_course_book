users = ['admin', 'tor', 'greta', 'linnea', 'ben']
if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user.title() + ", there is no new updates.")
        elif user:
            print("Welcome " + user.title() + "!")
else:
    print("We need to find some users!")
# checking if list is empty
# if not, print greetings to each on the list
# print a special greeting to admin

users = []
if users:
    for user in users:
        print("Welcome " + user.title() + ".")
else:
    print("We need to find some users!")
# the position of the indentation is very important
