# using arbitrary keyword arguments
def build_profile(first, last, **user_info):
    # creating parameters which include two positional arguments
    # and one arbitrary. **user_info creates an empty dictionary
    # where it stores any given key-value pair
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    # adding key-value pairs to an empty dictionary
    # first_name equals the first argument
    profile['last_name'] = last
    # last_name equals the second argument
    for key, value in user_info.items():
        # looping through the dictionary user_info
        profile[key] = value
        return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)
