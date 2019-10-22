# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik"
__email__ = "jonkors@nmbu.no"


class LCGRand:
    def __init__(self, seed):
        self.seed = [seed]
        self.a = 7**5
        self.m = 2**31-1
        self.idx = 0

    def rand(self):
        self.idx += 1
        self.seed.append((self.a * self.seed[self.idx - 1]) % self.m)
        return self.seed[self.idx]


class ListRand:
    def __init__(self, list_of_numbers):
        self.list = list_of_numbers
        self.a = 7 ** 5
        self.m = 2 ** 31 - 1
        self.idx = 0
        self.rand_list = []

    def rand(self):
        self.idx += 1
        if self.idx == len(self.list):
            raise RuntimeError(
                'There are no more numbers to generate randomness from. \
                Try starting a new instance with a new list of numbers'
            )
        self.rand_list.append((self.a * self.list[self.idx - 1]) % self.m)
        return self.rand_list[self.idx]
