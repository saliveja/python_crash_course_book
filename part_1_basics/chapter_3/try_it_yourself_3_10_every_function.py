
shoppinglist = ['eggs', 'milk', 'cheese', 'yogurt', 'almond butter', 'butter', 'soda water', 'coconut cream', 'broccoli', 'onion', 'cauliflower', 'mushrooms', 'carrots', 'garlic', 'ginger', 'earl gay', 'coffee', 'cream']
print(shoppinglist)

message = "\n\n" + str(sorted(shoppinglist))
print(message)

message = "\n\n" + str(sorted(shoppinglist, reverse=True))
print(message)


shoppinglist.reverse()
message = "\n\nThis is the shoppinglist for this week!"
print(message)
print(shoppinglist)



