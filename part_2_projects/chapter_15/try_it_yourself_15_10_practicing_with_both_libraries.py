# import matplotlib.pyplot as plt
# from die import Die
#
# die = Die()
# # creating an instance of class Die
# results = []
# # making a list to store results
#
# for roll_num in range(1000):
#     # rolling the die a hundred times
#     result = die.roll()
#     # the result is the method in Die called roll
#     # the method only returns a random result between one and number of sides
#     # int his case six
#     results.append(result)
#     # adding the result to the list
#
# frequencies = []
# # storing the number of times each value is rolled
#
# for value in range(1, die.num_sides + 1):
#     # we loop through all numbers on the die
#     # +1 is so that the same number won't be counted every time
#     frequency = results.count(value)
#     # counting how many times the value is selected
#     frequencies.append(frequency)
#     # appending the count to the list frequencies
#
# x_values = list(range(1, die.num_sides + 1))
# y_values = frequencies
# # number 1 to 6
# # plotly doesn't accept range directly which is why we need to
# # convert to a variable
# plt.style.use('seaborn')
# # >>> import matplotlib.pyplot as plt
# # >>> plt.style.available
# # to see the available styles
# fig, ax = plt.subplots()
# # subplots() exists within pyplot
# # can generate one or more plots within the same figure
# # variable fig represent the entire figure (the collection of plots)
# # variable represent a single plot
# ax.plot(x_values, y_values, linewidth=3)
# # plotting the data
# # linewidth makes the line thicker than default
# ax.set_title("Result of rolling one D6 1000 times", fontsize=24)
# # The overall title at the top
# ax.set_xlabel("Number", fontsize=14)
# # title on horizontal axis
# ax.set_ylabel("Frequency", fontsize=14)
# # title on vertical axis
# ax.tick_params(axis='both', labelsize=14)
# # styles the tick marks on both axis
#
# plt.show()

from plotly.graph_objs import Bar, Layout
from plotly import offline
from random import choice


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """initialize attributes of a walk."""

        self.num_points = num_points
        # default number of points in a walk is 5000
        self.x_values = [0]
        self.y_values = [0]
        # all walks start at 0

    def fill_walk(self, x_distance=0, y_direction=-1):
        """Calculate all the points in the walk."""
        self.x_distance = x_distance
        self.y_direction = y_direction

        while len(self.x_values) < self.num_points:
            # while the length of self.x_values is less than 5000
            # if self.x_distance == 0:
            self.x_distance = choice([0, 1, 2, 3, 4])
            # the distance is within range 0-5

            x_direction = choice([1, -1])
            # the choice of direction is -1 left or 1 right
            x_step = x_direction * self.x_distance
            # one step is direction multiplied with the distance
            self.y_direction = choice([1, -1])

            y_distance = choice([0, 1, 2, 3, 4])
            y_step = self.y_direction * y_distance
            # y axis had the same possibility of choices as x axis

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            # [-1] refers to index and means the last input in the list
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            # adding x to the list
            self.y_values.append(y)
            # adding y to the list

    def display_result(self):
        """Displaying result on a bar chart."""

        data = [Bar(x=self.x_values, y=self.y_values)]
        x_axis_config = {'title': 'Randomized x'}
        y_axis_config = {'title': 'Randomized y'}
        my_layout = Layout(title='Random walk',
                           xaxis=x_axis_config, yaxis=y_axis_config)

        offline.plot({'data': data, 'layout': my_layout},
                     filename='random_walk.html')


rw = RandomWalk()
rw.fill_walk()
rw.display_result()
