from random import randint

class Die:
    "A class representing single Die"

    def __init__(self,numside = 6):
        """Assume six sided."""
        self.num_sides = numside

    def roll(self):
        """Return a random value between 1 and 6"""
        return randint(1,self.num_sides)