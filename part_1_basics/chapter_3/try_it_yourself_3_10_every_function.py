
shoppinglist = ['eggs', 'milk', 'cheese', 'yoghurt', 'almond butter', 'butter', 'soda water', 'coconut cream', 'broccoli', 'onion', 'cauliflower', 'mushrooms', 'carrots', 'garlic', 'ginger', 'earl gay', 'coffee', 'cream']
print(shoppinglist)

shoppinglist.append('sweet potatoes')
print(shoppinglist)
# adding item at the end of the list

message = "\n\n" + str(sorted(shoppinglist))
print(message)
# sorting list in alphabetical order which is reversable

message = "\n\n" + str(sorted(shoppinglist, reverse=True))
print(message)
# sorting list in reverse, but non-permanent order

shoppinglist.reverse()
message = "\n\nThis is the shoppinglist for this week!"
print(message)
print(shoppinglist)
# reverse() is permanent

message = "\n\n"
shoppinglist.sort()
print(message + str(shoppinglist))
# to put things together (for example add a message to our list, we need to use str. print(message + shoppinglist) wouldn't be an understandable command.

shoppinglist.insert(3,'apples')
shoppinglist.insert(0, 'almond drink')
print(shoppinglist)
# inserting item at position 3 on the list

message = "\n\n"
shoppinglist.sort(reverse=True)
print(message + str(shoppinglist))
# sort() is permanent

print("The " + shoppinglist[1] + " didn't arrive yet.")

message = " didn't arrive yet."
print(shoppinglist.pop(1) + message)
print(shoppinglist)
# printing which item didn't arrive at at the same time remove the item.

del shoppinglist[1]
print(shoppinglist)
# deleting soda water from the list

shoppinglist.remove('yoghurt')
print(shoppinglist)
# removing yoghurt from the list. Great if one doesn't know the position of the item

remove_item = shoppinglist.pop(1)
print(shoppinglist)
print(remove_item)
#removing mushrooms from the list and printing which item was removed







