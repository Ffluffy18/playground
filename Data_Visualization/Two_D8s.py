import plotly.express as px

from die import Die

die_1 = Die(8)
die_2 = Die(8)

# outcome of the sum of two D8 rolled n times
results = []
for values in range(100000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


max_value = die_1.num_sides + die_1.num_sides

# how frequent the outcomes occur
frequencys = []
for value in range(2, max_value + 1):
    frequency = results.count(value)
    frequencys.append(frequency)

fig = px.bar(x=range(2, max_value + 1), y=frequencys)
fig.show()
