import json


def favorite_number():
    """Input and saving favorite number."""
    filename = 'number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number


def new_number():
    """Prompt for input on favorite number"""
    number = input("Enter your favorite number: ")
    filename = 'number.json'
    with open(filename, 'w') as f:
        json.dump(number, f)
    return number


def favorite_number_message():
    """Printing message with favorite number."""
    number = favorite_number()

    if number:
        print(f"I know your favorite number, it's {number}!")
    else:
        number = new_number()
        print(f"Your favorite number is {number}!")


favorite_number_message()
