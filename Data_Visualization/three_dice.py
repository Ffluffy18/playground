import plotly.express as px

from die import Die

dice_1 = Die()
dice_2 = Die()
dice_3 = Die()

# roll the dice and store outputs
results = []
for values in range(10000):
    result = dice_1.roll() + dice_2.roll() + dice_3.roll()
    results.append(result)


# store how frequent each value occurs
frequencies = []
max_value = dice_1.num_sides + dice_2.num_sides + dice_3.num_sides
for value in range(3, max_value + 1) :
    frequency = results.count(value)
    frequencies.append(frequency)

# mapping it
title = ('Probability of rolling three D3 dice 10,000 times')
labels = {'x': 'Result', 'y':'Frequency of result'}
fig = px.bar(x=range(3, max_value + 1), y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
