import matplotlib.pyplot as plt

input_values = [1,2,3,4,5,6]
squares = [1, 4, 9, 16, 25 , 36]
plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.plot(input_values,squares, linewidth = 3)

# set chart title and label axes.
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize  =14 )

# When  you  give  plot()  a  sequence  of  numbers,  it  assumes  the  first  data
# point  corresponds  to  an  x-coordinate  value  of  0,  but  our  first  point
# corresponds  to  an  x-value  of  1
# set Size of tick labels
ax.tick_params(axis = 'both', labelsize = 14)


plt.show() # matplotlib's pytplot library is resposible to show the plots.