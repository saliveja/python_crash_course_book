# checking if a certain value is in the list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
# if the user is not on the list banned_users then a message will be printed\
# including the users name

banned_users = ['andrew', 'carolina', 'david']
user = 'andrew'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
else:
    print(" good try!")
# if the user is on the list on banned_users the else option will be printed
