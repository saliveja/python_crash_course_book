# moving items from one list to another
# using pop(), append(), sort()

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# creating an empty list where we move confirmed users

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    # with pop() we are able to remove from the list of unconfirmed users
    # and still be able to work with the item
    # pop() removes from the end of the list

    print(f"Verifying user: {current_user.title()}")
    # the current user is the one that was removed from unconfirmed users
    confirmed_users.append(current_user)
    # adding to the list of current users

confirmed_users.sort()
# organizing the list in alphabetical order
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    # printing the users that have just been moved to the list of \
    # confirmed users
