import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
# x values are the numbers to be squared
y_values = [1, 4, 9, 16, 25]
# contains the square of each number
# the points to be plotted:
# (1,1), (2,4), (3,9) etc

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=200)
# 200 is the size of the dots
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)

ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()
