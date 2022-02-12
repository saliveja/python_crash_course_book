current_users = ['sara', 'tor', 'greta', 'linnea', 'ben']
new_users = ['dylan', 'kim', 'athena', 'tor', 'linnea']
for new_user in new_users:
    if new_user.lower() in current_users:
        # this means to check if any if new_users is among all of current users
        print("The username you have chosen is not available.")
    else:
        print("This username is available."
              " You are registered as "
              + new_user.title())
        # all users also in the current user list will receive message
        # that the chosen username is unavailable
        # for those who don't exist in current user will receive a message
        # message that the username is available and that they are registered
