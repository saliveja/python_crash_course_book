
shoppinglist = ['eggs', 'milk', 'cheese', 'yogurt', 'almond butter', 'butter', 'soda water', 'coconut cream', 'broccoli', 'onion', 'cauliflower', 'mushrooms', 'carrots', 'garlic', 'ginger', 'earl gay', 'coffee', 'cream']
print(shoppinglist)

shoppinglist.append('sweet potatoes')
print(shoppinglist)
# adding item at the end of the list

message = "\n\n" + str(sorted(shoppinglist))
print(message)
# sorting in alphabetical order, not permanent

message = "\n\n" + str(sorted(shoppinglist, reverse=True))
print(message)
#  organizing list reversed but not permanent

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
# inserting apples at position 3 and almond drink at position 0 on the list

message = "\n\n"
shoppinglist.sort(reverse=True)
print(message + str(shoppinglist))
# sort() is permanent

print("The " + shoppinglist[1] + " didn't arrive yet.")
# printing an item (sweet potatoes) that didn't yet arrive


message = " didn't arrive yet."
print(shoppinglist.pop(1) + message)
print(shoppinglist)
# printing which item didn't arrive at at the same time remove the item.

del shoppinglist[1]
print(shoppinglist)
# deleting soda water from the list

shoppinglist.remove('butter')
print(shoppinglist)
# removing yoghurt from the list. Great if one doesn't know the position of the item in the list

remove_item = shoppinglist.pop(1)
print(shoppinglist)
print(remove_item)
#removing mushrooms from the list and printing which item was removed

already_arrived = 'eggs'
	# QUESTION:
	# How to add more items, so they get bth printed as "arrived"
	# And they will be removed together from the list, 
	# seems like I can only do one at a time
shoppinglist.remove(already_arrived)
print("\n\nThese items already arrived: " + already_arrived + ".")
print("\n\nThis is the current version of the list:\n" + str(shoppinglist) + "\nThere are " + str(len(shoppinglist)) + " items left to be aquired.")

print(shoppinglist [-1])
del shoppinglist[-1]
print(shoppinglist) 
# deleting the last item on the list

shoppinglist[2] = 'books'
print(shoppinglist)



