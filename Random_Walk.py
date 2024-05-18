from random import choice

class RandomWalk:
    """A class to generate random walk"""
    def __init__(self,num_points = 5000):
        """Initialise walk attributes"""
        self.num_points = num_points

        # All walk starts at (0,0)
        self.x_walks = [0]
        self.y_walks = [0]

    def fill_walks(self):
        """Calculate all the points in the walk."""

        # Keep taking the steps until reached a desired length
        while len(self.x_walks) < self.num_points:

            self.get_step()
            # Rejects the steps that go nowhere,
            if self.x_steps==0 and self.y_steps==0:
                continue
            # calculate the new position 
            x = self.x_walks[-1] + self.x_steps
            y = self.y_walks[-1] + self.y_steps

            self.x_walks.append(x)
            self.y_walks.append(y)

    def get_step(self):
            # Decide which direction to go and how far to go in that direction
            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([-1,1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance 

            self.x_steps = x_step
            self.y_steps = y_step