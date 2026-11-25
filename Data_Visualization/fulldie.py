import random
import matplotlib.pyplot as plt


data = []
results = range(1, 7)
frequencies = []


for x in range(1000):
    result = random.randint(1, 6) 
    data.append(result)


for value in results:
    frequency = data.count(value)
    frequencies.append(frequency)

fig, ax = plt.subplots()
ax.bar(results, frequencies)
plt.show()
