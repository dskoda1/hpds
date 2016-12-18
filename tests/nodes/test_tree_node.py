from ..context import hpds
from hpds.nodes import TreeNode

import unittest


class TestTreeNode(unittest.TestCase):
    """Tree node tests."""

    def test_construction(self):
        val = 5
        node = TreeNode(val)

        self.assertEqual(node.value, val)

    def test_ptrs(self):
        vals = [5,3,6]
        nodes = [TreeNode(val) for val in vals]
        parent = nodes[0]
        parent.left, parent.right = nodes[1], nodes[2]

        self.assertEqual(parent.left.value, nodes[1].value)
        self.assertEqual(parent.right.value, nodes[2].value)

    def test_equality(self):
        node_one, node_two = TreeNode(4), TreeNode(4)
        self.assertEqual(node_one, node_two)
        diff = TreeNode(2)
        self.assertNotEqual(node_one, diff)


if __name__ == '__main__':
    unittest.main()
