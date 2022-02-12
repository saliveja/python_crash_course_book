alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
    points = 5
elif 'yellow' in alien_color:
    points = 10
elif 'red' in alien_color:
    points = 15
print("You've earned " + str(points) + "points.")
# using elif to test if 'green', 'yellow' and 'red is in the list.
# Because it's a chain with elif, it's stops after one statement is true

if 'green' in alien_color:
    print("You've earned 5 points.")
if 'yellow' in alien_color:
    print("You've earned 10 points.")
if 'red' in alien_color:
    print("You've earned 15 points.")
    # all three if statements are true and all three options are printed

alien_color = 'yellow'
# changing from list of colors to variable with value 'yellow'
if 'green' in alien_color:
    points = 5
if 'yellow' in alien_color:
    points = 10
else:
    points = 15
print("You've earned " + str(points) + " points.")
# printing "You've earned 10 points."
