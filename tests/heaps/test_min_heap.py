from ..context import hpds
from hpds.heaps import MinHeap

from random import randint
from sys import maxsize

import unittest


class TestMinHeap(unittest.TestCase):
    """Min heap tests."""

    def setUp(self):
        self.heap = MinHeap()

    
