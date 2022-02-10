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
