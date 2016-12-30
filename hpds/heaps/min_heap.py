from math import floor


class MinHeap(object):

    def __init__(self):
        self._values = [None]

    def insert(self, value):
        self._values.append(value)
        self._heapify(len(self._values) - 1)

    def pop(self):
        self._swap(len(self._values) - 1, 1)
        ret = self._values.pop()
        # Swap the root down the tree until heap prop
        # is satisfied
        if len(self._values) == 1:
            return ret

        current = 1
        while True:
            val = self._values[current]
            left = self._left_child(current)
            right = self._right_child(current)
            if left is not None and right is not None:
                if left <= right and val > left:
                    next_idx = self._left_child_index(current)
                elif right <= left and val > right:
                    next_idx = self._right_child_index(current)
                else:
                    break
            elif left is not None and right is None and left < val:
                next_idx = self._left_child_index(current)
            elif right is not None and left is None and right < val:
                next_idx = self._right_child_index(current)
            else:
                break

            self._swap(next_idx, current)
            current = next_idx

        return ret
    def _heapify(self, i):
        value = self._values[i]
        parent = self._parent(i)
        # Swap the value with its parent while the following
        # conditional holds true
        current = i
        while parent != None and parent > value:
            parent_index = self._parent_index(current)
            self._swap(current, parent_index)

            # set parent again
            current = parent_index
            parent_index = self._parent_index(parent_index)
            parent = self._values[parent_index] if parent_index else None

    def _swap(self, i, j):
        self._values[i], self._values[j] = \
            self._values[j], self._values[i]

    def _left_child_index(self, i):
        return  2 * i

    def _left_child(self, i):
        index = self._left_child_index(i)
        if index > len(self._values) - 1:
            return None
        return self._values[index]

    def _right_child_index(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        index = self._right_child_index(i)
        if index > len(self._values) - 1:
            return None
        return self._values[index]

    def _parent_index(self, i):
        i = float(i)
        return int(floor(i / 2))

    def _parent(self, i):
        index = self._parent_index(i)
        return self._values[index]
