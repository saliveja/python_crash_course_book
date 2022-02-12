guests = ['lena', 'anna', 'greta', 'nihad', 'can']
name = 'nihad'
if name in guests:
    print("Hello " + name.title() + "!")
else:
    print("Sorry, you are not on the invitation list.")

guests = ['lena', 'anna', 'greta', 'nihad', 'can']
name = 'bengt'
if name in guests:
    print("Hello " + name.title() + "!")
else:
    print("Sorry, you are not on the invitation list.")

foods = ['apple', 'cheese', 'soda', 'cream']
'apple' in foods
# True
'meat' in foods
#  False

number_1 = 32
number_2 = 44
number_3 = 23
number_4 = 22
number_1 >= 50 and number_4 >= 20
# both variables need to meet the conditions, but only number_4 do
number_1 >= 50 or number_4 >= 20
# number_1 don't meet the conditions but number_4 do which is enough
# only one of them need to meet the conditions
if number_3 == 23:
    print("I told you so")
else:
    print("Everybody hurts, sometimes")

if number_3 == 53:
    print("I told you so")
else:
    print("Everybody hurts, sometimes")

sport = 'boxing'
sport == 'aikido'
# first defines sport. second asks is sport is aikido which is false
sport == 'boxing'
# is True

place = 'ROME'
place.lower() == 'rome'
# this make all letters in variable place lower case letters. It is True
place.upper() == 'rome'
# this make all letters in variable place upper case letter. It is False

dessert = "blueberry pie"
if dessert != 'strawberry pie':
    print("I'm sorry, but I ordered a strawberry pie!")
    # if the variable dessert is not strawberry pie, print message

food_list = ['apple', 'cheese', 'soda', 'cream']
food = 'cream'
if food in food_list:
    print("I love " + food + "!")
else:
    print("Without cream there is no life")
    # if cream is in the list, we print "I love cream!"
    # if it isn't, we print "Without cream there is no life"

food_list = ['apple', 'cheese', 'soda', 'cream']
food = 'pasta'
if food in food_list:
    print("I love " + food + "!")
else:
    print("Without cream there is no life")
    # food != cream, it's pasta so else statement is printed

number = 1
number_1 = range(2, 10)
number_2 = range(11, 20)
if number_1 or number_2 == number:
    print("True")
    # with if statement, we use == because we are asking a question
3 in number_1
# Will return True because range is 2,10
1 in number_1
# return False

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

X1 = 10
X2 = 15
if X1 == 10:
    print(my_foods)
else:
    print(friend_foods)

X1 = 10
X2 = 15
if X1 == 13:
    print(my_foods)
else:
    print(friend_foods)
    # if X1 is 13 (which is False) then it will print my_foods
    # if it's not, it will print friends_food
