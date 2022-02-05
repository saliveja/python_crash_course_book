
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
# [:] refers to the whole my_foods list
# if we remove [:] the two lists will be printed exactly the same
# we want the two list to have a new and each a different item added

my_foods.append('cannoli')
friend_foods.append('ice cream')
# adding a new item on each list

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
# the two prints show the same list because one = the other


