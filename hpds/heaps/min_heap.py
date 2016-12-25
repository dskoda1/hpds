from math import floor


class MinHeap(object):

    def __init__(self):
        self._values = [None]


    def _left_child(self, i):
        index = 2 * i
        if index > len(self._values) - 1:
            return None
        return self._values[index]

    def _right_child(self, i):
        index = 2 * i + 1
        if index > len(self._values) - 1:
            return None
        return self._values[index]

    def _parent(self, i):
        i = float(i)
        index = int(floor(i / 2))
        return self._values[index]
