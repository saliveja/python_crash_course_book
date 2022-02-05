
pizzas = ['vezuvio', 'hawaii', 'calzone']
friend_pizzas = pizzas[:]
# this defines that pizzas and friend_pizzas look the same

pizzas.append('detroit')
print(pizzas)
# adding detroit to pizzas

friend_pizzas.append('st louis')
print(friend_pizzas)
# adding st louis to friend_pizzas

print("My favorite pizzas are:")
for pizza in pizzas[:]:
	print(pizza.title())
print("\n\n")
# printing statement and the list pizzas in a for loop

print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza.title())
	# printing statement about the friends favorite pizzas in a for loop.
