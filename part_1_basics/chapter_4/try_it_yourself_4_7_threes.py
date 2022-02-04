
threes = []
for value in range(1,31):
	threes.append(value*3)
print(threes)	
# using a for loop to print numbers 1-30 multiplied by three 


threes = [value*3 for value in range(1,31)]
for three in threes:
	print(three)
	# trying more concise code to print numbers 1-30 multiplied by three
	# first for value in range is definition, the second is the loop
