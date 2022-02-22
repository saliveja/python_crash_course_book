def member_list(first, last, **more_info):
    """Making a dictionary storing information about members."""
    more_info['First name'] = first
    more_info['Last name'] = last
    # adding the first two parameters to the dictionary

    for key, value in more_info.items():
        # looping through arbitrary arguments
        more_info[key] = value
        return more_info
