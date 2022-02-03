
pizzas = ['vezuvio', 'hawaii', 'calzone']
for pizza in pizzas:
	print(pizza.title())
	print(pizza.title() + ", is a funny name for a pizza.\n")

print("When I was a child, I really loved " + pizzas[0].title())
print("I don't really remember " + pizzas[pizzas.index('calzone')].title() + ", but there is one which is folded that is great!")
# how to point to an item on the list which we don't know the position of?

print(pizzas.index('hawaii'))
# to know the index number of a specific item
# list[list.index('nameofitem')] --> if we want to print the name directly in the message
print("Fruit on pizzas like " + pizzas[1] + " is not something that I would recommend.")
