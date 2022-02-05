
pizzas = ['vezuvio', 'hawaii', 'calzone']
friend_pizzas = pizzas[:]

pizzas.append('detroit')
print(pizzas)

friend_pizzas.append('st louis')
print(friend_pizzas)

print("My favorite pizzas are:")
for pizza in pizzas[:]:
	print(pizza.title())
