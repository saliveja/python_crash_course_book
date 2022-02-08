# tests for equality and inequality


# tests using the lower() function


# Numerical test on inequality and equality, greater and lesser than, greater \
# than and equal to and lesser than or equal to

marie = 40
danny = 18
marie <= 21 and danny >= 15
marie >= 21 and danny >= 15
marie > 45 or danny < 60

# test using the and keyword and the or keyword


# test whether an item is in the list
colors = ['red', 'black', 'green', 'purple', 'white', 'grey']
for color in colors:
    if color == 'black':
        print(color.upper())

# test whether an item is not in the list
colors = ['red', 'black', 'green', 'purple', 'white', 'grey']
color = 'black'
if color not in colors:
    print('Oh no!')
else:
    (color + " is my favorite color")
