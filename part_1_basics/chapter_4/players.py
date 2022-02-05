
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# print players 1, 2 and 3

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
# printing part of a list is called slices


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
# printing the first four
# It is included as in last exercise, the last number is not printed
# when first index isn't specified it starts from the beginning of the list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
# when the index at the end is not specified - 
# it will be printed until the end of the list  

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
# print the third last players on the list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
	# print the three first players each on a new line
	# specifying which numbers is dont direcly in for line 


