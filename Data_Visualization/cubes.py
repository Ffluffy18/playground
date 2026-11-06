import matplotlib.pyplot as plt

x_values = []
y_values = []

for x in range(1, 5000):
    x_values.append(x)
    y_values.append(x**3)


plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Wistia)
ax.axis([0, x, 0, (x**3)])
ax.ticklabel_format(style='sci')

plt.show()
