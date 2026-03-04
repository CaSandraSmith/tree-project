#!python3

from avltreenode import AvlTreeNode
import unittest


class AvlTreeNodeTest(unittest.TestCase):

    def test_init_and_properties(self):
        word = "hello"
        node = AvlTreeNode(word)
        # Verify node data
        assert isinstance(node.word, str)
        assert node.word == word
        # Verify next_words is empty list
        assert node.next_words == []
        # Verify left node is None
        assert node.left is None
        # Verify right node is None
        assert node.right is None
        # Verify height data
        assert node.height == 0