import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
# using the ending json to show that the data is stored
# in json format
with open(filename, 'w') as f:
    # opening file in write mode
    json.dump(numbers, f)
