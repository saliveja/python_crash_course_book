import matplotlib.pyplot as plt

x_values = range(1, 1001)
# x values are the numbers to be squared
# range is 1-1000
y_values = [x ** 2 for x in x_values]
# contains the square of each number
# making a for loop for the calculation
# x**2 is square
# results stored in y_values

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# s variable defines the size of the dots
# c defines the color which can be expressed like 'red', 'green' etc
# or with RGB color model. 0 produces dark colors and values
# closer to 1 lighter colors
# cmap=plt.cm.Blues results in lower y values are lighter blue
# and the higher values are darker blue

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)

ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 1100, 0, 1100000])
# axis method requires four values
# the minimum and the maximum values for the x and y axis
# specifying the range for each axis
plt.show()
# if we want to save the plot to a file we can instead of show() use:
# plt.savefig('squares_plot.png', bbox_inches='tight')
# 'squares_plot.png' is the filename
# bbox_inches='tight' takes away whitespace around the plot
