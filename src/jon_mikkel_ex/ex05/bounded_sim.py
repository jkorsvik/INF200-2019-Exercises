# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik"
__email__ = "jonkors@nmbu.no"

from src.jon_mikkel_ex.ex05.walker_sim import Walker, Simulation


class BoundedWalker:
    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.walker = Walker(start, home)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def is_within_bounds(self):
        """
        Checks whether the walkers position is in between the outer limits
        :return: Boolean
        """
        return self.left_limit < self.walker.get_position() < self.right_limit

    def move_within_bounds(self):
        position_before_moving = self.walker.get_position()
        self.walker.move()
        if self.is_within_bounds(self.walker.get_position()):
            return
        self.walker.position = position_before_moving


class BoundedSimulation:
    def __init__(self, start, home, seed, left_limit, right_limit):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.simulation = Simulation(start, home, seed)

    def walk_bounded(self):
        while True:
            self.simulation 
            if self.bounded_walker.walker.is_at_home():
                return self.bounded_walker.walker.is_at_home()

    def run_bounded_sim(self, num_walks):
        list_of_steps = []

        for walk in range(num_walks):
            list_of_steps.append(self.single_walk())

        return list_of_steps
