import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50_000)
    # increasing the number of points to 50 000 from 5000
    rw.fill_walk()
    # making an instance of the class RandomWalk

    plt.style.use('classic')
    # using the style classic
    fig, ax = plt.subplots(figsize=(15, 9), dpi=72)
    # variable representing the whole figure and a single plot
    # figsize is setting the size of the figure
    # if we know the resolution (dpi), we can add this parameter to make
    # more efficient use of available space
    point_numbers = range(rw.num_points)
    # referring to the variable in RandomWalk, defining the number to 5000
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=1)
    # c=point_numbers said that the points in RandomWalk should be colored
    # the chosen color is blue
    # ew.x_values etc is the list starting with default value 0
    # removing the black edge of each point
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    # set the starting point to 0, 0 with color green and in size 100
    # instead of 15
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
               edgecolors='none', s=100)
    # the last point, which is defined by the index -1, is red and size 100
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    # removing both axis
    plt.show()

    keep_running = input("Make another walk? y/n: ")
    if keep_running == 'n':
        break
