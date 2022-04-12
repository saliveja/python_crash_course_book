import matplotlib.pyplot as plt
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

x_values = list(range(1, die.num_sides + 1))
y_values = frequencies
# number 1 to 6
# plotly doesn't accept range directly which is why we need to
# convert to a variable
plt.style.use('seaborn')
# >>> import matplotlib.pyplot as plt
# >>> plt.style.available
# to see the available styles
fig, ax = plt.subplots()
# subplots() exists within pyplot
# can generate one or more plots within the same figure
# variable fig represent the entire figure (the collection of plots)
# variable represent a single plot
ax.plot(x_values, y_values, linewidth=3)
# plotting the data
# linewidth makes the line thicker than default
ax.set_title("Result of rolling one D6 1000 times", fontsize=24)
# The overall title at the top
ax.set_xlabel("Number", fontsize=14)
# title on horizontal axis
ax.set_ylabel("Frequency", fontsize=14)
# title on vertical axis
ax.tick_params(axis='both', labelsize=14)
# styles the tick marks on both axis

plt.show()
