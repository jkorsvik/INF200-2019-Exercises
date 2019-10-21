# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik"
__email__ = "jonkors@nmbu.no"


class LGCRand:
    def _init__(self, seed):
        self.seed = seed
        self.a = 7**5
        self.m = 2**31-1
        self.n = 0

    def rand(self):
        self.n += 1
        self.seed[self.n] = (self.a * self.seed[self.n - 1]) % self.m
        return self.seed




