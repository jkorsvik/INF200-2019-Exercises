# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik"
__email__ = "jonkors@nmbu.no"


class LCGRand:
    slope = 7 ** 5
    congruence_class = 2 ** 31 - 1

    def __init__(self, seed):
        """

        :param seed: A number selected when initializing, integer, set into
        a list.
        a: is a large odd number
        m: is a large odd number
        """
        self.hidden = seed

    def rand(self):
        """
        Index (idx) is updated each time rand is called. The seed list is
        appended with the newly calculated "random number" based on the
        first seed.
        :return: the last seed from the list. list of integers
        """
        self.hidden *= self.slope
        self.hidden %= self.congruence_class
        return self.hidden

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        """
        Generate an infinite sequence of random numbers.

        Yields
        ------
        int
            A random number.
        """
        while True:
            yield self.rand()
        # Alternatively you could:
        # return RandIter(self, 0)
        # The code can handle both ways


class RandIter:

    def __init__(self, random_number_generator, length):
        """
        Arguments
        ---------
        random_number_generator :
        A random number generator with a ``rand`` method that
        takes no arguments and returns a random number.
        length : int
        The number of random numbers to generate
        """
        self.generator = random_number_generator
        self.length = abs(length)
        self.num_generated_numbers = None

    def __iter__(self):
        """
        Initialise the iterator.

        Returns
        -------
        self : RandIter

        Raises
        ------
        RuntimeError
            If iter is called twice on the same RandIter object.
        """
        if self.num_generated_numbers is not None:
            raise RuntimeError(
                'Can only initialise the iterator for the object once.')
        self.num_generated_numbers = 0
        return self

    def __next__(self):
        """
        Generate the next random number.

        Returns
        -------
        int
            A random number.

        Raises
        ------
        RuntimeError
            If the ``__next__`` method is called before ``__iter__``.
        StopIteration
            If ``self.length`` random numbers are generated.
        """
        if self.num_generated_numbers is None:
            raise RuntimeError('The iterator has to be called before function\
 next')
        if self.length > 0:
            if self.num_generated_numbers == self.length:
                raise StopIteration('The length of sequence of numbers has\
 been met')
        rand_number = self.generator.rand()
        self.num_generated_numbers += 1
        return rand_number


if __name__ == "__main__":
    rand_number_generator = LCGRand(1)
    for rand in rand_number_generator.random_sequence(10):
        print(rand)

    for i, rand in enumerate(rand_number_generator.infinite_random_sequence()):
        print(f'The {i:3}-th random number is {rand}')
        if i > 100:
            break
