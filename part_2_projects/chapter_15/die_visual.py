from plotly.graph_objs import Bar, Layout
from plotly import offline
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
# number 1 to 6
# plotly doesn't accept range directly which is why we need to
# convert to a variable
data = [Bar(x=x_values, y=frequencies)]
# bars displaying the values and their frequency
# bar is a class in plotly when formatting data to a bar chart
# a data set can have multiple elements, therefore we need to wrap in []

x_axis_config = {'title': 'Result'}
# title on the x axis is Result
y_axis_config = {'title': 'Frequency of result'}
# title on the y axis is Frequency of result
my_layout = Layout(title='Results of rolling one D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
# layout id the overall visual of the graph
# title is the overall title of the graph
# xaxis and yaxis are the side labels
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
# offline needs a dictionary containing the data
# and accepts a file name where we will store the output

# print(frequencies)
