# moving items from one list to another

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# creating an empty list where we move confirmed users

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    # with pop() we are able to remove from the list of unconfirmed users
    # and still be able to work with the item

    print(f"Verifying user: {current_user.title()}")
    # the current user is the one that was removed from unconfirmed users
    confirmed_users.append(current_user)
    # adding to the list of current users
