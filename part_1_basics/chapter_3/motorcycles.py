# changing, adding and removing elements in a list

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

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

# insert adds elements at the designated place in the list. In the example above space is made a the index position, number 0.

# removing elements from a list

motorcycles = ['honda' , 'yamaha' , 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
# del means delete/remove from list, [0] indicated position that should be deleted

motorcycles = ['honda' , 'yamaha' , 'suzuki']
del motorcycles[1]
print(motorcycles)
