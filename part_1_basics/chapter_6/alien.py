# a simple dictionary
alien_0 = {'color': 'green', 'points': 5}
# dictionary storing different values about a particular item
print(alien_0['color'])
print(alien_0['points'])
# printing 'green' and '5'
# a dictionary wrapps the information in {}
# a key-value pair is a set of value associated with each other
# every key is connected to its value by a colon
# the key-value pairs are separated by commas
# one key value pair is {'color': 'green'}
# 'color' is a key and the value is 'green'
# we can store as many as we want

# starting with an empty directory
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
# adding values to the dictionary
print(alien_0)
# this prints the dictionary as one line:
# {'color': 'green', 'points': 5}

# accessing values in a dictionary
print(alien_0['color'])
# this print the value green only
new_points = alien_0['points']
# new points equals alien_0 points which is 5
print('You just earned ' + str(new_points) + ' points!')

# adding new key-value pair
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x position'] = 0
alien_0['y position'] = 25
print(alien_0)

# starting with an empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
# works like adding a new key-value pair
# normally we start with empty dictionaries

# modifying values in a dictionary
alien_0 = {'color': 'green'}
print('The alien is now ' + alien_0['color'] + '.')

alien_0['color'] = 'yellow'
print('The alien is now ' + alien_0['color'] + '.')
