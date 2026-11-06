import matplotlib.pyplot as plt

num = 0
x_values = [] 
y_values = [] 

# make square values for lists
while num < 1000:
   num += 1
   x_values.append(num)
   y_values.append(num ** 2)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, color=(0, .8, 0))

# Set chart title and label axes.
ax.set_title("Square numbers", fontsize=24)
ax.set_ylabel("Square value", fontsize=14)
ax.set_xlabel("value", fontsize=24)

# Set size of tick labels
# ax.tick_params("x", zorder=10)

# Set the range for each axis
ax.axis([0, 1100, 0, 1000000])
ax.ticklabel_format(style='plain')

plt.show()
