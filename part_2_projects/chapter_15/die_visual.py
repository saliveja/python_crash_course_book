from die import Die

die = Die()
# creating an instance of class Die
results = []
# making a list to store results

for roll_num in range(1000):
    # rolling the die a hundred times
    result = die.roll()
    # the result is the method in Die called roll
    # the method only returns a random result between one and number of sides
    # int his case six
    results.append(result)
    # adding the result to the list

frequencies = []
# storing the number of times each value is rolled

for value in range(1, die.num_sides + 1):
    # we loop through all numbers on the die
    # +1 is so that the same number won't be counted every time
    frequency = results.count(value)
    # counting how many times the value is selected
    frequencies.append(frequency)
    # appending the count to the list frequencies

print(frequencies)
