import matplotlib.pyplot as plt
from Random_Walk import RandomWalk 

# Keep making new random walks as long as the program is active:
while True:
    rw = RandomWalk(50000)
    rw.fill_walks()

    # Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9), dpi = 64)                  # Matplotlib assumes that your screen resolution is 100 pixels per inch
    point_numbers = range(rw.num_points)

    ax.scatter(rw.x_walks,rw.y_walks,c=point_numbers,cmap=plt.cm.Blues, edgecolors = 'none', s = 1) # edgecolors is none to get rid of black boundary
    """
    #ax.plot(rw.x_walks,rw.y_walks, linewidth = 3)

    # set chart title and label axes.
    #ax.set_title("Square Numbers", fontsize = 24)
    #ax.set_xlabel("Value", fontsize = 14)
    #ax.set_ylabel("Square of Value", fontsize  =14 )
    """
    # Emphasize the first and last point,
    ax.scatter(0,0,c='green',edgecolors = 'none',s=100)         
    ax.scatter(rw.x_walks[-1],rw.y_walks[-1],c='red',edgecolors = 'none',s=100)

    # Remove the axes
    #ax.get_xaxis().set_visible(False)
    #ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Would you like to make another plot?(y,n): ")
    if keep_running == 'n':
        break