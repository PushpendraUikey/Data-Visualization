import matplotlib.pyplot as plt
from Random_Walk import RandomWalk 

rw = RandomWalk()
rw.fill_walks()

# Plot the points in the walk
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_walks,rw.y_walks,c='Green', s = 15)

plt.show()