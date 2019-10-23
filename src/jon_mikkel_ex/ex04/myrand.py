# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik"
__email__ = "jonkors@nmbu.no"


class LCGRand:
    def __init__(self, seed):
        """

        :param seed: A number selected when initiliazing, integer, set into
        a list.
        a: is a large odd number
        m: is a large odd number
        """
        self.seed = [seed]
        self.a = 7**5
        self.m = 2**31-1
        self.idx = 0

    def rand(self):
        """
        Index (idx) is updated each time rand is called. The seed list is
        appended with the newly calculated "random number" based on the
        first seed.
        :return: the last seed from the list. list of integers
        """
        self.idx += 1
        self.seed.append((self.a * self.seed[self.idx - 1]) % self.m)
        return self.seed[self.idx]


class ListRand:
    def __init__(self, list_of_numbers):
        self.list = list_of_numbers
        self.idx = 0

    def rand(self):
        if self.idx == len(self.list):
            raise RuntimeError(
                'There are no more numbers to generate randomness from. \
                Try starting a new instance with a new list of numbers'
            )
        self.idx += 1
        return self.list[self.idx - 1]  # Returns the right number from list
