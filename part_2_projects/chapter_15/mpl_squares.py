import matplotlib.pyplot as plt

# importing pyplot as plt

squares = [1, 4, 9, 16, 25]
# list containing a square number sequence
fig, ax = plt.subplots()
# subplots() exists within pyplot
# can generate one or more plots within the same figure
# variable fig represent the entire figure (the collection of plots)
# variable represent a single plot
ax.plot(squares)
# plotting the data

plt.show()
# opens Matplotlib's viewer to show the data
