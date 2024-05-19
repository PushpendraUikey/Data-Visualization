from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# die = Die()         # six sided die
# create a D6 and a D10 dice
die_1 = Die()
die_2 = Die(10)
# Make some roll no's and store results in a list.
results = []

for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(2,max_result+1))       #Plotly doesn’t accept the results of the range() function
                                                #directly, so we need to convert the range to a list explicitly using the list()
                                                #function.

data = [Bar(x=x_values,y=frequencies)]
x_axis_config = {'title':'Result', 'dtick':1}
y_axis_config = {'title': 'Frequencies of Result'}
my_layout = Layout(title='Results of rolling a D6 and D10 dice 1000 times',xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data,'layout':my_layout}, filename='D6_D10.html')
print(frequencies)