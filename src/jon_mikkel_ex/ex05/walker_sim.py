# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik"
__email__ = "jonkors@nmbu.no"

from random import getrandbits, seed as random_seed


class Walker:
    """
    Walker class, with methods for checking position and moving.
    Has its own method for finishing a trip home.
    :param start_place: initial position of the walker
    :param home: position of the walker's home
    """
    def __init__(self, start_place, home):
        self.position = start_place
        self.home = home
        self.steps = 0

    def move(self):
        """
        Uses a really efficient cointoss-  bool(getrandbits(1)) gives true or
        false. Registers each move as a step.
        """
        if bool(getrandbits(1)):
            self.position += 1
        else:
            self.position -= 1
        self.steps += 1

    def is_at_home(self):
        """ Checks if position is equal to home
        :returns True or False: bool
        """
        return self.position == self.home

    def get_position(self):
        """
        :returns position: Current position of walker
        """
        return self.position

    def get_steps(self):
        """
        :returns steps: Number of steps taken by walker
        """
        return self.steps

    def make_the_trip(self):
        """
        Walker moves until is_at_home is true
        :return: get_steps: Number of steps taken until final position
        """
        while True:
            self.move()
            if self.is_at_home():
                return self.get_steps()


class Simulation:
    def __init__(self, start_place, home, rand_seed=None):
        """
        Initialise the simulation

        Arguments
        ---------
        start_place : int
        The walker's initial position
        home : int
        The walk ends when the walker reaches home
        rand_seed : int
        Random generator seed
        """
        self.walker = Walker(start_place, home)
        self.seed = random_seed(rand_seed)

    def single_walk(self):
        """
        Walker moves until is_at_home is true
        :return: get_steps: Number of steps taken until final position
        """
        return self.walker.make_the_trip()

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
        The number of walks to simulate

        Returns
        -------
        list[int]
        List with the number of steps per walk
        """
        list_of_steps = []

        for walk in range(num_walks):
            list_of_steps.append(self.single_walk())

        return list_of_steps


if __name__ == "__main__":
    number_of_walks = 20
    list_of_seeds = [12345, 12345, 54321]
    list_start_and_end = ((0, 10), (10, 0))
    for seed in list_of_seeds:
        for start, end in list_start_and_end:
            exp_walk = Simulation(start, end, seed)
            print(exp_walk.run_simulation(number_of_walks))
