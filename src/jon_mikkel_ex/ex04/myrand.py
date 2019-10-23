# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik"
__email__ = "jonkors@nmbu.no"

from pprint import pprint


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
    """
    Class that input a list and output that same list for each call of rand
    :param: list_of_numbers - a list of numbers
    """
    def __init__(self, list_of_numbers):
        self.list = list_of_numbers
        self.idx = 0

    def rand(self):
        if self.idx == len(self.list):
            raise RuntimeError(
                'There are no more numbers to generate "randomness" from. \
                Try starting a new instance with a new list of numbers'
            )
        self.idx += 1
        return self.list[self.idx - 1]  # Returns the right number from list


if __name__ == "__main__":
    list_rand_test = ListRand([1, 43534534, 76589234, 1245])
    print('Testing the ListRand Class: \n'
          '----------------------------')
    for x in range(1, 5):
        print(f' {x}. Random number -> {list_rand_test.rand()}')

    lgc_rand = LCGRand(123)
    print('                 \n '
          ' Testing the LCG Class with 123 as seed: \n'
          '----------------------------')
    for y in range(1, 11):
        print(f' {y}. Random number -> {lgc_rand.rand()}')

    print('\n'
          'The list of all random numbers generated and used for the next: \n'
          '-----------------------------')
    pprint(lgc_rand.seed)
