import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    # making an instance of the class RandomWalk

    plt.style.use('classic')
    # using the style classic
    fig, ax = plt.subplots()
    # variable representing the whole figure and a single plot
    point_numbers = range(rw.num_points)
    # referring to the variable in RandomWalk, defining the number to 5000
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=15)
    # c=point_numbers sayd that the points in RandomWalk should be colored
    # the chosen color is blue
    # ew.x_values etc is the list starting with default value 0
    # removing edge color
    plt.show()

    keep_running = input("Make another walk? y/n: ")
    if keep_running == 'n':
        break
