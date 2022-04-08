import matplotlib.pyplot as plt

# importing pyplot as plt

squares = [1, 4, 9, 16, 25]
# list containing a square number sequence
fig, ax = plt.subplots()
# subplots() exists within pyplot
# can generate one or more plots within the same figure
# variable fig represent the entire figure (the collection of plots)
# variable represent a single plot
ax.plot(squares, linewidth=3)
# plotting the data
# linewidth makes the line thicker than default
ax.set_title("Square Numbers", fontsize=24)
# The overall title at the top
ax.set_xlabel("Value", fontsize=14)
# title on horizontal axis
ax.set_ylabel("Square of value", fontsize=14)
# title on vertical axis
ax.tick_params(axis='both', labelsize=14)
# styles the tick marks on both axis

plt.show()
# opens Matplotlib's viewer to show the data
