#!python3

from avltreenode import AvlTreeNode
import unittest


class AvlTreeNodeTest(unittest.TestCase):

    def test_init_and_properties(self):
        data = 5
        node = AvlTreeNode(data)
        # Verify node data
        assert isinstance(node.data, int)
        assert node.data == data
        # Verify left node is None
        assert node.left is None
        # Verify right node is None
        assert node.right is None
        # Verify height data
        assert node.height == 0