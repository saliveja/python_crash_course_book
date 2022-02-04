
threes = []
for value in range(3,31,3):
	threes.append(value)
print(threes)	
# using a for loop to print numbers 1-30 multiplied by three 


threes = [value for value in range(3,31,3)]
for three in threes:
	print(three)
	# trying more concise code to print numbers 1-30 multiplied by three
	# first for value in range is definition, the second is the loop
