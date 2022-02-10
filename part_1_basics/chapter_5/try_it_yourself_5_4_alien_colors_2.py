# if-else chain
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print("You just earned 5 points")
else:
    print('You just earned 10 points')

alien_color = ['green', 'yellow', 'red']
if 'black' in alien_color:
    points = 5
else:
    points = 10
print('You just earned ' + str(points) + '.')
