from die import Die

die = Die()
# creating an instance of class Die
results = []
# making a list to store results

for roll_num in range(100):
    # rolling the die a hundred times
    result = die.roll()
    # the result is the method in Die called roll
    # the method only returns a random result between one and number of sides
    # int his case six
    results.append(result)
    # adding the result to the list

print(results)
