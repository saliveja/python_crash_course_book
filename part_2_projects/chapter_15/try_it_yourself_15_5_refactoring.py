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

    def fill_walk(self):
        """Calculate all the points in the walk."""

        while len(self.x_values) < self.num_points:

            [x_step, y_step] = self.get_step()
            x = self.x_values[-1] + x_step
            # [-1] refers to index and means the last input in the list
            y = self.y_values[-1] + y_step

            if x_step == 0 and y_step == 0:
                continue

            self.x_values.append(x)
            # adding x to the list
            self.y_values.append(y)
            # adding y to the list

    def get_step(self):
        x_distance = choice([0, 1, 2, 3, 4])
        # the distance is within range 0-5
        x_direction = choice([1, -1])
        # the choice of direction is -1 left or 1 right
        x_step = x_direction * x_distance
        # one step is direction multiplied with the distance
        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4])
        y_step = y_direction * y_distance
        # y axis had the same possibility of choices as x axis

        return [x_step, y_step]

#
# rw = RandomWalk(20)
# rw.fill_walk()
