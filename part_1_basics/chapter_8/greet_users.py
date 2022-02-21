# passing a list
def greet_users(names):
    # parameter 'names'
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello,  {name.title()}!"
        print(msg)
        # for each name in names, 'msg' will be printed


usernames = ['hanna', 'ty', 'margot']
# creating a list will all users which will be greeted
greet_users(usernames)
# this connects to the function because usernames are outside the for loop
# inside the function we described what we want to happen
# when we call the function we point to who it is directed to
