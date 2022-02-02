
places = ['Hongkong' , 'Tibet', 'Peru', 'Canada', 'Iceland']
print(places)
# the first unsorted list

print(sorted(places))
# sorting in alphabetical order with sorted()

print(places)
# the original list again, to see that it hasn''t been permanently changed

print(sorted(places, reverse=True))
# printing the list i reverse order 

print(places)
# showing that the original list hasn't been permanently changed

places.reverse()
print(places)
# using reverse() to reverse the order of the list permanently

places.reverse()
print(places)
# using reverse() again to put the list back to original state

places.sort()
print(places)
# sorting the list in alphabetical order permanently

places.sort(reverse=True)
print(places)

