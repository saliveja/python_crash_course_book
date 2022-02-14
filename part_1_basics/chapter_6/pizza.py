pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# toppings contain a list
print("You ordered a " + pizza['crust'] + "-crust pizza" +
      "with the following toppings:")
# printing sentence with value
for topping in pizza['toppings']:
    print("\t" + topping)
    # pizza['toppings'] directing to value
