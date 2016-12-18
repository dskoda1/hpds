from ..context import hpds
from hpds.trees import BinarySearchTree
from hpds.nodes import TreeNode

import unittest


class TestBinarySearchTree(unittest.TestCase):
    """Binary search tree tests."""

    def setUp(self):
        self.bst = BinarySearchTree()
        self.bst.insert(10)

    def test_insert_root(self):
        bst = BinarySearchTree()
        bst.insert(5)

        self.assertEqual(bst.root.value, 5)

    def test_insert_returns_node(self):
        bst = BinarySearchTree()
        node = bst.insert(7)

        self.assertEquals(node.value, 7)

    def test_insert_less(self):
        bst = self.bst
        node = bst.insert(6)
        self.assertEqual(bst.root.left, node)

    def test_insert_greater(self):
        bst = self.bst
        node = bst.insert(12)
        self.assertEqual(bst.root.right, node)

    def test_insert_repeat_noop(self):
        bst = self.bst
        node = bst.insert(10)
        self.assertEqual(bst.root, node)
        self.assertIsNone(bst.root.left)
        self.assertIsNone(bst.root.right)


    def test_preorder(self):
        bst = BinarySearchTree()
        vals = [1,4,5,7,10,12,15,19]
        for val in vals:
            bst.insert(val)

        tree_vals = bst.preorder_values()
        self.assertEqual(vals, tree_vals)


if __name__ == '__main__':
    unittest.main()
