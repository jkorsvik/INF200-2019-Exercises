# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik"
__email__ = "jonkors@nmbu.no"

from random import getrandbits


class Walker:
    def __init__(self, the_club, home):
        self.position = 0
        self.home = home
        self.start = the_club
        self.steps = 0

    def move(self):
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
