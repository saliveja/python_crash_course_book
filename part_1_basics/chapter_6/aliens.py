# nesting
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
# making a dictionary with three aliens
aliens = [alien_0, alien_1, alien_2]
# including the three aliens in a list

for alien in aliens:
    print(alien)
    # printing the list

aliens = []
# creating an empty list
for alien_number in range(30):
    # defining ow many time to loop:
    # each time a new alien is created
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    # adding a new alien and key-value pairs to the dictionary
    aliens.append(new_alien)
    # adding the new alien to the list

for alien in aliens[0:3]:
    # for the first three aliens
    if alien['color'] == 'green':
        # if the aliens color is green
        alien['color'] = 'yellow'
        # it will be changed to yellow
        alien['speed'] = 'medium'
        # and the speed will be changed from slow to medium
        alien['points'] = 10
        # the points will change from 5 to 10

print("\n")
for alien in aliens[:5]:
    # creating a for loop to print the first five aliens
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))
# printing the total number of aliens
