from ..nodes import TreeNode

class BinarySearchTree(object):
    """Implementation of a binary search tree. Provides the following api:

    - .root (property) Returns the root of the tree
    - .insert(integer: value) (maintains bst properties)
    """

    def __init__(self):
        self._root = None

    def insert(self, value):
        node = TreeNode(value)
        if self._root is None:
            self._root = node
        else:
            self._insert(self._root, node)
        return node

    def _insert(self, check_node, insert_node):
        if check_node.value == insert_node.value:
            return
        elif check_node.value > insert_node.value:
            if check_node.left is None:
                check_node.left = insert_node
            else:
                self._insert(check_node.left, insert_node)

        elif check_node.value < insert_node.value:
            if check_node.right is None:
                check_node.right = insert_node
            else:
                self._insert(check_node.right, insert_node)
        


    @property
    def root(self):
        return self._root
