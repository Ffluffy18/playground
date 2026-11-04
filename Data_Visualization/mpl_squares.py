import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8-darkgrid')
figure, axes = plt.subplots()
axes.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
axes.set_title("Square Numbers", fontsize=24)
axes.set_xlabel("Value", fontsize=14)
axes.set_ylabel("Squares of Value", fontsize=14)

# Set size of tick labels.
axes.tick_params(labelsize=14)

plt.show()
