import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = (0.23,0.253,0.845), s = 10)  # To change the color of the points, pass c to scatter() with the name of a color ex: c='red'
# You can also define custom colors using the RGB color model. To define
# a color, pass the c argument a tuple with three decimal values (one each for
# red,  green,  and  blue  in  that  order),  using  values  between  0  and  1. ex: c = (0,0.4,0.694)

# set chart title and label axes.
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# set size of tick labels
ax.tick_params(axis='both',which= 'major',labelsize =14)

# set the range for each axis.
ax.axis([0,1100,0,1100000])
plt.show()


# plot() function makes straight lines between two consecutive points and scatter() function makes a point at their location
