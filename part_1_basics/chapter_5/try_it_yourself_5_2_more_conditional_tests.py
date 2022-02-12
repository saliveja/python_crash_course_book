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
    # printing "Thank you for packing my hoodie"
print("\n")
clothes = 'Hoodie'
clothes.lower() == 'hoodie'
# lower() function changes the letter i variable 'clothes' to lower case
# without lower() the conditional test would be False


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
# marie bigger than 45 or danny smaller than 60 --> True

# test whether an item is in the list
colors = ['red', 'black', 'green', 'purple', 'white', 'grey']
for color in colors:
    if color == 'black':
        print(color.upper())
        # using for loop. If the color black is in the list, print black in \
        # upper case letters
print("\n")
# test whether an item is not in the list
colors = ['red', 'black', 'green', 'purple', 'white', 'grey']
color = 'black'
if color not in colors:
    print('Oh no!')
else:
    print(color.title() + " is my favorite color")
    # if the color black is not in colors, print "Oh no!" and if it is\
    # print "Black is my favorite color"

print("\n\n")

# EXCERCISE PROGRAM 3 - for @saliveja:
# application for log in layers
# Define a list of comrades - with 8 comrades
# make another database mirroring the xweser comrades in the contact list
# make a variable which defines loggin of comrades
# make a variable which defines password for comrades
# make a variable for xweser comrades and a password for xweser comrades
# make a variable user - a field which anyone can fill and
# user password
# Print a message to the user if their name and password do not match the list
# print a message for the user if they loged in as a comrade
# Print a message if they log in as a xweser comrade
# Print a message for the system - to quickly categorize the user like:
# user comrade == True/False
# user xweser comrade == True/False

comrades = ['anna', 'berit', 'janne', 'can', 'emma', 'kalle', 'samuel',
            'fiona']
xweser_comrades = ['anna', 'berit', 'emma', 'fiona']
password_comrades = 'hejgej'
password_xweser = 'untilallarefree'
user = 'emma'
password = 'hejgej'
if user in comrades and password is password_comrades:
    print("Hello " + user.title() + ", welcome to our intranet!")
else:
    print("I'm sorry, but you are not registered")
print(user.lower() in comrades and password == password_comrades)

user = 'fiona'
password = 'untilallarefree'
if user in xweser_comrades and password is password_xweser:
    print("To change society we have to kill the dominant mindset")
else:
    print("I'm sorry but you are not registered")
print(user.lower() in xweser_comrades and password == password_xweser)

user = 'fiona'
password = 'killthedominantmindset'
if user in xweser_comrades and password is password_xweser:
    print("To change society we have to kill the dominant mindset")
else:
    print("I'm sorry but you are not registered")
print(user.lower() in xweser_comrades and password == password_xweser)

user = 'emma'
password = 'hejgej'
if user.lower() in comrades and password == password_comrades:
    print("Great to see you, " + user.title())
print(user.lower() in comrades and password == password_comrades)

# EXCERCISE PROGRAM 3 - layers of log in:
# application for log in layers
# Define a list of comrades - with 8 comrades
# make another database mirroring the xweser comrades in the contact list
# make a variable which defines loggin of comrades
# make a variable which defines password for comrades
# make a variable for xweser comrades and a password for xweser comrades
# make a variable user - a field which anyone can fill and
# user password
# Print a message to the user if their name and password do not match the list
# print a message for the user if they loged in as a comrade
# Print a message if they log in as a xweser comrade
# Print a message for the system - to quickly categorize the user like:
# user comrade == True/False
# user xweser comrade == True/False

# The important point is to focus ont the first step where:
# the list_comrades and list_xweser_comrades are empty
# over time we have new users registering
# those are getting index as comrade_x or comrade_xweser_x
# the MAIN FOCUS - how do we add them to the list in the simpliest way
# withot .append() every single one of them manually

list_comrades = []
list_xweser_comrades = []

comrade_1 = 'aaa1'
comrade_2 = 'aaa2'
comrade_3 = 'aaa3'
comrade_4 = 'aaa4'
comrade_xweser_1 = 'bbb1'
comrade_xweser_2 = 'bbb2'
comrade_xweser_3 = 'bbb3'

list_comrades.extend(
    value for name, value in locals().items() if name.startswith('comrade'))
# The locals() method updates and returns a dictionary of the current \
# local symbol table.
# These include variable names, methods, classes, etc.
# items() --> used to return the list with all dictionary keys with values
# this adds every new value that starts with comrades which is also \
# printed sorted

list_xweser_comrades.extend(
    value for name, value in locals().items() if name.startswith \
        ('comrade_xweser'))

print(list_comrades)

# DID NOT WORK:
# ~for comrade in [comrade_(str(range(1, 100)))]:
# ~    list_comrades.append(comrade)

# ~comrade_x = list(str("comrade_" + str(range(1, 100))))
# ~for comrade in comrade_x:
# ~    list_comrades.append(comrade)

print(list_xweser_comrades)
# print(list_xweser_comrades)
