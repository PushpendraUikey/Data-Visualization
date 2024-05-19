from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die = Die()         # six sided die

# Make some roll no's and store results in a list.
results = []

for roll_num in range(1001):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(1,die.num_sides+1))       #Plotly doesn’t accept the results of the range() function
                                                #directly, so we need to convert the range to a list explicitly using the list()
                                                #function.

data = [Bar(x=x_values,y=frequencies)]
x_axis_config = {'title':'Result'}
y_axis_config = {'title': 'Frequencies of Result'}
my_layout = Layout(title='Result of rolling one D6 1000 times',xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data,'layout':my_layout}, filename='D6.html')