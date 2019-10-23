# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik"
__email__ = "jonkors@nmbu.no"

from random import getrandbits
from pprint import pprint


class Walker:
    """
    Walker class, with methods for checking position and moving.
    Has its own method for finishing a trip home.

    Input
    ------
    The club(starting position) - integer
    Home(ending position) - integer
    """
    def __init__(self, the_club, home):
        self.position = the_club
        self.home = home
        self.steps = 0

    def move(self):
        """
        Uses a really efficient cointoss-  bool(getrandbits(1)) gives true or
        false. Registers each move as a step.
        :return: New position after move
        """
        if bool(getrandbits(1)):
            self.position += 1
        else:
            self.position -= 1
        self.steps += 1
        return self.position

    def is_at_home(self):
        return self.position == self.home

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.steps

    def make_the_trip(self):
        while True:
            self.move()
            if self.is_at_home():
                return self.get_steps()


if __name__ == "__main__":
    """
    Making a list of the distances and making nested for-loop(woopsie)
    for creating a dictionary over the number of steps for 5 experiments for 
    each distance.
    
    Prints out a list of the number of steps per distance
    """
    num_sim = 5
    list_of_distances = [1, 2, 5, 10, 20, 50, 100]
    dict_of_path_lengths = dict()
    for end in list_of_distances:
        path_length = []
        for _ in range(num_sim):  # Experiments per distance
            walkiehomie = Walker(0, end)  # ex: 0-100 = 100 distance
            path_length.append(walkiehomie.make_the_trip())
        dict_of_path_lengths[end] = path_length
        pprint(
            f'Distance: {end} -> Path lengths : {dict_of_path_lengths[end]}'
            )
