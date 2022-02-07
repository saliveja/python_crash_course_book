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
