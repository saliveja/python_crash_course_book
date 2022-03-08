# moving items from one list to another
# using pop(), append(), sort()

class Users():

    def __init__(self, current_user, confirmed_users, unconfirmed_users):
        """Class moving items from one list to another."""
        self.user = current_user
        self.confirmed = confirmed_users
        self.unconfirmed = unconfirmed_users

    def poppingUser(self):
        while self.unconfirmed:
            self.user = self.unconfirmed.pop()
            # with pop() we are able to remove from the list of
            # unconfirmed users and still be able to work with
            # the item. pop() removes from the end of the list

    def verifyingUser(self):
        """Printing the verified users."""
        print(f"Verifying user: {self.user.title()}")
        # the current user is the one that was removed from unconfirmed users
        self.confirmed.append(self.user)
        # adding to the list of current users

    def printUsers(self):
        self.confirmed.sort()
        # organizing the list in alphabetical order
        print("\nThe following users have been confirmed:")
        for user in self.confirmed:
            print(user.title())
            # printing the users that have just been moved to the list of \
            # confirmed users
