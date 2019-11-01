# -*- coding: utf-8 -*-

__author__ = 'Hans Ekkehard Plesser'
__email__ = 'hans.ekkehard.plesser@nmbu.no'

"""
Acceptance test suite for EX04.

Your code should pass these tests before submission.
"""

import pytest
from src.jon_mikkel_ex.ex04.myrand import LCGRand, ListRand
from src.jon_mikkel_ex.ex04.walker import Walker


def test_lcg():
    """Test that LCG works."""

    lcg = LCGRand(346)
    assert lcg.rand() == 5815222
    assert lcg.rand() == 1099672039


def test_list_rng():
    """Test that ListRNG generator works."""
    numbers = [4, 5, 29, 11]
    lr = ListRand(numbers)
    assert [lr.rand() for _ in range(len(numbers))] == numbers
    with pytest.raises(RuntimeError):
        lr.rand()


def test_walker():
    """ Testing walking class for proper function"""
    start, home = 10, 20
    w = Walker(start, home)
    assert not w.is_at_home()
    w.move()
    assert w.get_position() != start
    w.move()
    assert w.get_steps() == 2
