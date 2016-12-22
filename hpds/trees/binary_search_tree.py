from ..nodes import TreeNode
import collections

class BinarySearchTree(object):
    """Implementation of a binary search tree. Provides the following api:

    - .root (property) Returns the root of the tree
    - .insert(integer: value) (maintains bst properties)
    """

    def __init__(self):
        self._root = None

    def insert(self, value, success_report=False):
        if not value:
            return None

        node = TreeNode(value)
        node, inserted = self._insert(self._root, node)

        if success_report:
            return node, inserted
        else:
            return node

    def insert_list(self, values):
        fail_count = 0
        for x in values:
            if x and self._is_iter(x):
                num_failed = self.insert_list(x)
                fail_count += num_failed
            else:
                node = TreeNode(x)
                node, inserted = self._insert(self._root, node)
                if not inserted:
                    fail_count += 1

        return fail_count

    def _insert(self, check_node, insert_node):
        inserted = False

        if not self._root:
            self._root = insert_node
            inserted = True
        elif check_node.value > insert_node.value:
            inserted = self._insert_to_side_of_node(check_node, 'left', insert_node)
        elif check_node.value < insert_node.value:
            inserted = self._insert_to_side_of_node(check_node, 'right', insert_node)
        elif check_node.value == insert_node.value:
            inserted = False
        return insert_node, inserted

    def _insert_to_side_of_node(self, check_node, side, insert_node):
        if not check_node[side]:
            check_node[side] = insert_node
            inserted = True
        else:
            inserted = self._insert(check_node[side], insert_node)

        return inserted
    def preorder_values(self):
        vals = []
        self._preorder_traversal(self._root, vals)
        return vals

    def _preorder_traversal(self, node, values):
        if node:
            self._preorder_traversal(node.left, values)
            values.append(node.value)
            self._preorder_traversal(node.right, values)

    def _is_iter(self, test):
        return isinstance(test, collections.Iterable)

    @property
    def root(self):
        return self._root
