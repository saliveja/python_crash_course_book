import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    print(f"Is your username {username}?")
    # verifying that the previous user is the same as the current
    answer = input("Enter yes or no: ")

    if answer.lower() == 'no':
        # if the answer is no, the user is asked to enter name
        username = get_new_username()
        # the user will be passed to the get_new_user function
        print(f"Welcome {username}!")
        # user greeted

    else:
        username = get_stored_username()
        # if the stored username and the current username is the same
        print(f"Welcome back {username}")
        # user will be greeted as someone who entered data before


greet_user()
