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
ax.scatter(x_values, y_values, s=10)
# s variable defines the size of the dots
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)

ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 1100, 0, 1100000])
# axis method requires four values
# the minimum and the maximum values for the x and y axis
# specifying the range for each axis
plt.show()
