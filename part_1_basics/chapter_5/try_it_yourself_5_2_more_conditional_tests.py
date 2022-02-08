# tests for equality and inequality
number = '16'
number == '25'
# False

item = 'Book'
item.lower() == 'book'
# True

# tests using the lower() function
clothes = ['tshirt', 'hoodie', 'pants', 'socks']
item = 'hoodie'
if item == 'tshirt':
    print("i would have preferred a hoodie")
else:
    print("Thank you for packing my " + item.lower())
# printing "Thank you for oacking my hoodie"

clothes = 'Hoodie'
clothes.lower() == 'hoodie'
# True bcs using lower() function

# Numerical test on inequality and equality, greater and lesser than, greater \
# than and equal to and lesser than or equal to
# test using the and keyword and the or keyword

marie = 40
danny = 18
marie <= 21 and danny >= 15
# conditional that if marie is lesser than or equal to 21 and danny is bigger\
# than or equal to 15 the statement will be True
marie >= 21 and danny >= 15
# marie bigger than or equal to 21 and danny bigger than or equal to 15 the\
# statement will be True
marie > 45 or danny < 60
# marie bigger than 45 or danny smaller than 60 - True

# test whether an item is in the list
colors = ['red', 'black', 'green', 'purple', 'white', 'grey']
for color in colors:
    if color == 'black':
        print(color.upper())
# using for loop. If the color black is in the list, print black in \
# upper case letters

# test whether an item is not in the list
colors = ['red', 'black', 'green', 'purple', 'white', 'grey']
color = 'black'
if color not in colors:
    print('Oh no!')
else:
    (color.title() + " is my favorite color")
# if the color black is not in colors, print "Oh no!" and if it is\
# print "Black is my favorite color"
