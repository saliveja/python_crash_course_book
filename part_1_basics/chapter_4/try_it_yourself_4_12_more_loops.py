

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')
# adding a new item on each list

print("My favorite foods are:")
for my_food in my_foods:
	print(my_food.title())

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
	print(friend_food.title())


