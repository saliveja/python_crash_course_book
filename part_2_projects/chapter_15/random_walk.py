from random import choice


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """initialize attributes of a walk."""

        self.num_points = num_points
        self.x_vales = 0
        self.y_values = 0
        # all walks start at 0