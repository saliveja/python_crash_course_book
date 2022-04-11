from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die()
die_2 = Die()
# creating two instances of class Die
results = []

for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    # multiplying the two die results
    results.append(result)

frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of result'}
my_layout = Layout(title='Results of rolling two D6 a 1000 times,'
                         'result multiplied', xaxis=x_axis_config,
                   yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout},
             filename='d6_d6_multiplied.html')
