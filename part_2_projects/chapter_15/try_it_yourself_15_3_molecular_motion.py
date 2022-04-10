import matplotlib.pyplot as plt
from try_it_yourself_15_5_refactoring import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw = RandomWalk(50000)
    # increasing the number of points to 50 000 from 5000
    rw.fill_walk()
    # making an instance of the class RandomWalk

    plt.style.use('dark_background')
    # using the style classic
    fig, ax = plt.subplots(figsize=(15, 9), dpi=72)
    # variable representing the whole figure and a single plot
    # figsize is setting the size of the figure
    # if we know the resolution (dpi), we can add this parameter to make
    # more efficient use of available space
    point_numbers = range(rw.num_points)
    # referring to the variable in RandomWalk, defining the number to 5000
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
               cmap=plt.cm.Purples, edgecolors='none', s=5)
    # c=point_numbers said that the points in RandomWalk should be colored
    # the chosen color is blue
    # ew.x_values etc is the list starting with default value 0
    # removing the black edge of each point
    ax.scatter(0, 0, c='purple', s=50)
    # set the starting point to 0, 0 with color green and in size 100
    # instead of 15
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', s=50)
    # the last point, which is defined by the index -1, is red and size 100
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    # removing both axis
    plt.show()

    keep_running = input("Make another walk? y/n: ")
    if keep_running == 'n':
        break
