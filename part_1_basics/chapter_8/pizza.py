def make_pizza(*toppings):
    # * creates an empty tuple and includes whatever value it receives
    """Print the list of toppings that have been requested."""
    print(toppings)


make_pizza('pepperoni')
# first time we call the function, we added one topping
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# second time we call the function we added three toppings


def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
