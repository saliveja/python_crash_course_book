request = "\nPlease enter all the toppings that you want on your pizza: "
# asking for input on which toppings are wanted on the pizza

while True:
    # as long as True the program will continue
    toppings = input(request)
    # toppings means the input in the request
    response = (f" I'll add {toppings} to your pizza!")
    # every time a new input on toppings is shared
    # a message confirming that the toppin has been added will be printed
    if toppings == 'quit':
        # if the user will write quit instead of a topping the program will stop
        print("\nThank you for your order!")
        # and this message will be printed instead
        break
        # break exits the program
    else:
        print(response)
        # if 'quit' is not written the program will continue
