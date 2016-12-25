from ..context import hpds
from hpds.heaps import MinHeap

from random import randint
from sys import maxsize

import unittest


class TestMinHeap(unittest.TestCase):
    """Min heap tests."""

    def setUp(self):
        self.heap = MinHeap()
        self.heap._values = [None] + \
            [i for i in range(1, 8)]

    def test_left_child(self):
        tuples = [
            (1, 2),
            (2, 4),
            (3, 6),
            (7, None),
        ]
        for x, y in tuples:
            self._test_equal_function(
                MinHeap._left_child, x, y)

    def test_right_child(self):
        tuples = [
            (1, 3),
            (2, 5),
            (3, 7),
            (7, None),
        ]
        for x, y in tuples:
            self._test_equal_function(
                MinHeap._right_child, x, y)

    def test_parent(self):
        tuples = [
            (7, 3),
            (6, 3),
            (5, 2),
            (4, 2),
            (3, 1),
            (2, 1),
            (1, None),
        ]
        for x, y in tuples:
            self._test_equal_function(
                MinHeap._parent, x, y)

    def _test_equal_function(self, func, x, y):
        self.assertEqual(func(self.heap, x), y)
