
threes = []
for value in range(1,31):
	threes.append(value*3)
print(threes)	
# using a for loop to print numbers 1-30 multiplied by three 


threes = [value*3 for value in range(1,31)]
for three in threes:
	print(three)
	# trying more concise code to print numbers 1-30 multiplied by three
	# with two for commands, is it a loop in a loop? how many can be used at one time?
