def build_profile(first, last, **profile):
    """Build a dictionary containing everything we know about a user."""
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in profile.items():
        profile[key] = value
        return profile


user_profile = build_profile('Maria (Marusha)', 'Nikiforova',
                             Occupation='Revolutionary',
                             Location='Ukraine',
                             Responsibility='Military command', )

print(user_profile)
