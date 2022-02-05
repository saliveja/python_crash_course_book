
items = ['hairbrush', 'tshirt', 'pants', 'socks', 'toothbrush', 'sweater', 'hoodie', 'glasses', 'shoes', 'computer', 'camera']
print("The first three items in the list are:")
for item in items[:3]:
	print(item.title())
print("\n\n")

print("Three items from the middle of the list are:")
for item in items[4:7]:
	print(item.title())
