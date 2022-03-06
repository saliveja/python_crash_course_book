import json

filename = 'numbers.json'

with open(filename) as f:
    # we don't define mode, so it opens automatically
    # in read mode
    numbers = json.load(f)
    # loading the information stored in the file

print(numbers)
