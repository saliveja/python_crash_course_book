
squares = []
# this defines an empty list calles squares
for value in range(1,11):
	# we are looping and using values from 1-10
	square = value**2
	# we are setting a variable inside the loop **2 (square)
	squares.append(square)
	# every new value is added to the list
	
print(squares)

squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)
# we can write squares.append(value**2) directly to be more concise
# sometimes it's easier to read when it's organized like line 6 and 8
# focus on writing code that is understandable first and not efficiency

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
#prints the smallest value
max(digits)
# prints the biggest value
sum(digits)
# prints the totals sum of values in the list

numbers = list(range(1, 500))
sum(numbers)
# printing 124750
