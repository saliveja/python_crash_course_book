import matplotlib.pyplot as plt

x_values = range(1, 5001)
# the numbers to plot
y_values = [x ** 3 for x in x_values]
# making a for loop for cubes

plt.style.use('dark_background')
# styling using seaborn deep
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.cool, s=10)
# cmap doesn't work with plot, but with scatter()
ax.set_title("Cubes", fontsize=20)
# main title Cubes
ax.set_ylabel('x**3 value', fontsize=10)
# y label x**3 value
ax.set_xlabel('value', fontsize=10)
# x label value
ax.tick_params(axis='both', labelsize=10)
# size for ticks on both axis is 10
ax.axis([0, 6000, 0, 125000000000])
# defining range, x until 6 and y until 125
plt.show()
