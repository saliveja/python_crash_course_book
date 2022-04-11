from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die()
die_2 = Die()
# creating two instances of class Die
results = [(die_1.roll() + die_2.roll()) for i in range(1000)]

max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]

x_values = list(range(2, max_result + 1))
# x_values is the range of the two dice
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
# dtick tells plotly to label every tick mark
y_axis_config = {'title': 'Frequency of result'}
# title on the y axis is Frequency of result
my_layout = Layout(title='Results of rolling two D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
# layout id the overall visual of the graph
# title is the overall title of the graph
# xaxis and yaxis are the side labels
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
# offline needs a dictionary containing the data
# and accepts a file name where we will store the output

# print(frequencies)
