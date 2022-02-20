# returning a dictionary
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    # creating a dictionary where the value is the parameter
    if age:
        person['age'] = age
        # if age in included in the dictionary person
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)
