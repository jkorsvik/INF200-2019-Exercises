# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik"
__email__ = "jonkors@nmbu.no"

from src.jon_mikkel_ex.ex05.walker_sim import Walker, Simulation


class BoundedWalker(Walker):
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
        self.left_limit = left_limit
        self.right_limit = right_limit
        super().__init__(start, home)

    def is_within_bounds(self):
        """
        Checks whether the walkers position is in between the outer limits
        :return: Boolean
        """
        return self.left_limit < self.get_position() < self.right_limit

    def move(self):
        position_before_moving = self.get_position()
        Walker.move(self)
        if self.is_within_bounds():
            return
        self.steps -= 1
        self.position = position_before_moving


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int or None
            Random generator seed
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.left_limit = left_limit
        self.right_limit = right_limit
        super().__init__(start, home, seed)

    def single_walk(self):
        """
        Walker moves until is_at_home is true
        :return: get_steps: Number of steps taken until final position
        """
        walker = BoundedWalker(
            self.start, self.home, self.left_limit, self.right_limit
                              )
        return walker.make_the_trip()

    def run_bounded_sim(self, num_walks):
        list_of_steps = []

        for _ in range(num_walks):
            list_of_steps.append(self.single_walk())

        return list_of_steps


if __name__ == "__main__":
  #  exp_walk = BoundedSimulation(0, 20, None, 20, 0)
   # print(exp_walk.run_simulation(20))
    walker = BoundedWalker(0, 20, 0, 20)
    print(walker.make_the_trip())
    """
    numb_of_walks = 20
    start, end, right_boundary = 0, 20, 20
    list_of_left_boundaries = [0, -10, -100, -1000, -10000]
    for left_boundary in list_of_left_boundaries:
        exp_walk = BoundedSimulation(
            start, end, None, right_boundary, left_boundary
                                    )
        print(f'Left boundary: {left_boundary} List of distances:\
        {exp_walk.run_simulation(numb_of_walks)}')
"""