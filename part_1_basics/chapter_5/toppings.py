# testing multiple conditions
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
# all three are independent tests and evaluated
# mushrooms andextra cheese are found in the list and are printed
# print last text message
# the code wouldn't work with elif since elif stops after a test passes
# because of this only mushrooms would be added and printed together\
# with the text message in the end

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
# using a for loop adding each item on the list to the pizza

print("\n")

# checking for special items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        # if the requested topping is green peppers,
        # it will be printed that we are out right now
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
        # all other items on the list will be added

print("\nFinished making your pizza!")

# checking that a list is not empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# using multiple lists
