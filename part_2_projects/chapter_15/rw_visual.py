import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
# making an instance of the class RandomWalk

plt.style.use('classic')
# using the style classic
fig, ax = plt.subplots()
# variable representing the whole figure and a single plot
ax.scatter(rw.x_values, rw.y_values, s=15)
# calling for the lists (with default 0) in RandomWalk
plt.show()
