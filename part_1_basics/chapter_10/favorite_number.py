import json


def favorite_number():
    """Input and saving favorite number."""
    filename = 'number.json'

    with open(filename, 'w') as f:
        number = input("What is your favorite number? ")
        return number
