import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
# the nnumbers to plot
y_values = [x ** 3 for x in x_values]
# making a for loop for cubes

plt.style.use('seaborn-deep')
# styling using seaborn deep
fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=3)
# using plot for graphics
ax.set_title("Cubes", fontsize=20)
# main title Cubes
ax.set_ylabel('x**3 value', fontsize=10)
# y label x**3 value
ax.set_xlabel('value', fontsize=10)
# x label value
ax.tick_params(axis='both', labelsize=10)
# size for ticks on both axis is 10
ax.axis([0, 6, 0, 125])
# defining range, x until 6 and y until 125
plt.show()
