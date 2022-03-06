import json
from favorite_number import favorite_number


def favorite_number_message():
    """Printing message with favorite number."""
    number = favorite_number()
    filename = 'number.json'

    with open(filename) as f:
        print(f"I know your favorite number, its {number}!")


favorite_number_message()
