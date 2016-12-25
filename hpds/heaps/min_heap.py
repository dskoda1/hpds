from math import floor


class MinHeap(object):

    def __init__(self):
        self._values = [None]


    def _left_child(self, i):
        return self._values[2 * i]

    def _right_child(self, i):
        return self._values[2 * i + 1]

    def _parent(self, i):
        i = float(i)
        index = int(floor(i / 2))
        return self._values[index]
