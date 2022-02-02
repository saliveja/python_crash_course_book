
# Organizing the list in alphabetical order woth sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# reverse alphabetical order
cars = ['bmw' , 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# sorted() list
# the sorted list will appear in alphabetical order
# It is not a permanent change and can also be used with reverse=true
cars = ['bmw' , 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars) 

# printing a list in reverse order with sorted() method
print(sorted(cars, reverse=True))

# reverse the order of the list with reverse() method
cars = ['bmw' , 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
# the list is shown with the last value first, but not in alphabetical order
# reverse() changes the list permanently, but it can be changed back any time with the same method
 


