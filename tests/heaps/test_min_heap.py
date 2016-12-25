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
        self._test_equal_function(
            MinHeap._left_child, 1, 2)
        self._test_equal_function(
            MinHeap._left_child, 2, 4)
        self._test_equal_function(
            MinHeap._left_child, 3, 6)

    def test_right_child(self):
        self._test_equal_function(
            MinHeap._right_child, 1, 3)
        self._test_equal_function(
            MinHeap._right_child, 2, 5)
        self._test_equal_function(
            MinHeap._right_child, 3, 7)

    def test_parent(self):
        self._test_equal_function(
            MinHeap._parent, 7, 3)
        self._test_equal_function(
            MinHeap._parent, 6, 3)
        self._test_equal_function(
            MinHeap._parent, 5, 2)
        self._test_equal_function(
            MinHeap._parent, 4, 2)
        self._test_equal_function(
            MinHeap._parent, 3, 1)
        self._test_equal_function(
            MinHeap._parent, 2, 1)
        self._test_equal_function(
            MinHeap._parent, 1, None)

    def _test_equal_function(self, func, x, y):
        self.assertEqual(func(self.heap, x), y)
