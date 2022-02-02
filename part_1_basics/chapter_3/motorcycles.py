# changing, adding and removing elements in a list
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
# above changes value from honda to ducati.


# appending/adding elements to the end of the list
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
 
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# inserting elements to a list
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
# insert adds elements at the designated place in the list. In the example above space is made a the first position, number 0 for ducati.

# removing elements from a list
motorcycles = ['honda' , 'yamaha' , 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
# del means delete/remove from list, [0] indicated position that should be deleted

motorcycles = ['honda' , 'yamaha' , 'suzuki']
del motorcycles[1]
print(motorcycles)

# removing item with pop() method
motorcycles = ['honda' , 'yamaha' , 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
# Line 44 and 45 communicate the removal of the last item, as missing from the list. Line 46 shows which item was removed.

motorcycles = ['honda' , 'yamaha' , 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycles I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print("The fist motorcycle I owned was a " + first_owned.title() + ".")
# pop can select any position to print. In this example position 0, the first position i selected to direct to information about which value was the first motorcycle.

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

first_owned = motorcycles[0]
print("The fist motorcycle I owned was a " + first_owned.title() + ".")

motorcycles = ['honda' , 'yamaha' , 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda' , 'yamaha' , 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles[1]
print(popped_motorcycle)
# Pop removes while [] only points to a position. 

motorcycles = ['honda' , 'yamaha' , 'suzuki' , 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
# the remove command gives information about which value to remove and then removes it, in the example 'ducati' is removed from the list.

motorcycles = ['honda' , 'yamaha' , 'suzuki' , 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
# with the name of the variable we can communicate the reason for removal, such a in this example.



