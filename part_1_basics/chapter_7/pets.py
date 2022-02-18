# using remove() to remove all instances of value from a list

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    # using the while loop to delete all 'cat' values in the list
    # the loop ensures that the loop continues until all 'cat' are removed
print(pets)
