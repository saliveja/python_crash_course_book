
# tuple
# values that cannot change are called immutable
# an immutable list is called a tuple


dimensions = (200, 50)
print(dimensions[0])
#printing value in first position
print(dimensions[1])
# printing value in the second position

dimensions[0] = 250
print(dimensions[0])
# the value of index 0 cannot be change,
# when it is defined in the first variable
# if we want immutable values for the rectangle;
# it is good that python communicates and error

dimensions = (200,50)
for dimension in dimensions:
	print(dimension)

# writing over a tuple
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
	# we can modify the tuple by writing a new variable
