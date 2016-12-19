from ..context import hpds
from hpds.trees import BinarySearchTree
from hpds.nodes import TreeNode

from random import randint
from sys import maxsize

import unittest


class TestBinarySearchTree(unittest.TestCase):
    """Binary search tree tests."""

    def setUp(self):
        self.bst = BinarySearchTree()
        self.bst.insert(value=10)

    def test_none_insert(self):
        self.assertIsNone(self.bst.insert())

    def test_insert_root(self):
        bst = BinarySearchTree()
        bst.insert(value=5)

        self.assertEqual(bst.root.value, 5)

    def test_insert_returns_node(self):
        bst = BinarySearchTree()
        node = bst.insert(value=7)

        self.assertEquals(node.value, 7)

    def test_insert_with_success_report(self):
        bst = BinarySearchTree()
        node, inserted = bst.insert(value=7, success_report=True)

        self.assertEquals(node.value, 7)
        self.assertTrue(inserted)

    def test_insert_less(self):
        bst = self.bst
        node = bst.insert(value=6)
        self.assertEqual(bst.root.left, node)

    def test_insert_greater(self):
        bst = self.bst
        node = bst.insert(value=12)
        self.assertEqual(bst.root.right, node)

    def test_insert_repeat_noop(self):
        bst = self.bst
        node = bst.insert(value=10)
        self.assertEqual(bst.root, node)
        self.assertIsNone(bst.root.left)
        self.assertIsNone(bst.root.right)

    def test_preorder(self):
        bst = BinarySearchTree()
        vals = [1,4,5,7,10,12,15,19]
        for val in vals:
            bst.insert(value=val)

        tree_vals = bst.preorder_values()
        self.assertEqual(vals, tree_vals)

    def test_large_case(self):
        bst = BinarySearchTree()
        vals = [randint(-100000000, 100000000) for x in range(10000)]
        for x in vals:
            bst.insert(value=x)

        uniq = set(vals)
        self.assertEqual(sorted(list(uniq)), bst.preorder_values())

    def test_insert_list(self):
        bst = BinarySearchTree()
        vals = [randint(-100000000, 100000000) for x in range(500)]
        bst.insert(values=vals)

        uniq = set(vals)
        self.assertEqual(sorted(list(uniq)), bst.preorder_values())

    def test_fail_count_insert_list(self):
        bst = BinarySearchTree()
        vals = [50, 23, 42, 50, 50]
        fail_count = bst.insert(values=vals)

        uniq = set(vals)
        self.assertEqual(sorted(list(uniq)), bst.preorder_values())
        self.assertEqual(fail_count, 2)

    def test_nested_lists(self):
        bst = BinarySearchTree()
        vals = [8, [3, 4, 5], 9]
        bst.insert(values=vals)
        vals = [8, 3, 4, 5, 9]
        self.assertEqual(sorted(vals), bst.preorder_values())

if __name__ == '__main__':
    unittest.main()
