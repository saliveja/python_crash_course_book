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
# this list could also be made as a tuple if there is a stable selection
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        # if the item in requested toppings is also on the list of available\
        # toppings, then it will be added
        # if not, then a message will be shared that we don't have it
        # because it's a for loop it will go through and check all items
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
