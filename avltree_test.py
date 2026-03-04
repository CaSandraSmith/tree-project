#!python3

from avltree import AvlTree, AvlTreeNode
import unittest


class AvlTreeTest(unittest.TestCase):
    def test_init_and_properties(self):
        tree = AvlTree()
        # Verify root node
        assert tree.root is None


    def test_insert(self):
        tree = AvlTree()
        tree.insert(5)
        # Verify root node
        assert isinstance(tree.root, AvlTreeNode)
        assert tree.root.data == 5
        assert tree.root.left is None
        assert tree.root.right is None


    def test_insert_with_multiple_nodes(self):
        tree = AvlTree()
        # Insert new number that starts from root node
        tree.insert(5)
        # Verify root node
        assert isinstance(tree.root, AvlTreeNode)
        assert tree.root.data == 5
        assert tree.root.left is None
        assert tree.root.right is None
        # Insert new number is larger than the root
        tree.insert(10)
        # Verify new node 10
        assert tree.root.right is not None
        assert tree.root.right.data == 10
        assert isinstance(tree.root.right, AvlTreeNode)
        assert tree.root.left is None
        # Insert new number is smaller than the root
        tree.insert(3)
        # Verify new node 3
        assert tree.root.left is not None
        assert tree.root.left.data == 3
        assert isinstance(tree.root.left, AvlTreeNode)
        

    def test_insert_can_perform_single_left_rotation(self):
        tree = AvlTree()
        # insert new node
        tree.insert(5)
        # Verify current root
        assert tree.root.data == 5
        # insert values that will cause left rotation
        tree.insert(27)
        tree.insert(45)
        # verify left rotation occurred
        assert tree.root.data == 27
        assert tree.root.left.data == 5
        assert tree.root.right.data == 45
    
    
    def test_insert_can_perform_single_right_rotation(self):
        tree = AvlTree()
        # insert new node
        tree.insert(45)
        # Verify current root
        assert tree.root.data == 45
        # insert values that will cause right rotation
        tree.insert(27)
        tree.insert(5)
        # verify right rotation occurred
        assert tree.root.data == 27
        assert tree.root.left.data == 5
        assert tree.root.right.data == 45
    
    
    def test_insert_can_perform_double_right_left_rotation(self):
        tree = AvlTree()
        # insert new node
        tree.insert(5)
        # Verify current root
        assert tree.root.data == 5
        # insert values that will cause right left rotation
        tree.insert(45)
        tree.insert(27)
        # verify right left rotation occurred
        assert tree.root.data == 27
        assert tree.root.left.data == 5
        assert tree.root.right.data == 45


    def test_insert_can_perform_double_left_right_rotation(self):
        tree = AvlTree()
        # insert new node
        tree.insert(45)
        # Verify current root
        assert tree.root.data == 45
        # insert values that will cause left right rotation
        tree.insert(5)
        tree.insert(27)
        # verify left right rotation occurred
        assert tree.root.data == 27
        assert tree.root.left.data == 5
        assert tree.root.right.data == 45


    def test_delete(self):
        tree = AvlTree()
        # insert new node
        tree.insert(5)
        # Verify root node
        assert tree.root.data == 5
        # delete node
        tree.delete(5)
        assert tree.root is None


    def test_delete_with_multiple_nodes(self):
        tree = AvlTree()
        # Insert multiple nodes
        tree.insert(5)
        tree.insert(10)
        # Verify root node
        assert tree.root.data == 5
        assert tree.root.right.data == 10
        # delete node
        tree.delete(5)
        assert tree.root.data == 10
        assert tree.root.right is None
        assert tree.search(5) is False


    def test_delete_can_perform_single_left_rotation(self):
        tree = AvlTree()
        # Insert multiple nodes
        tree.insert(5)
        tree.insert(3)
        tree.insert(10)
        tree.insert(15)
        # Verify current root
        assert tree.root.data == 5
        # remove value that will cause left rotation
        tree.delete(3)
        # verify left rotation occurred
        assert tree.root.data == 10
        assert tree.root.left.data == 5
        assert tree.root.right.data == 15


    def test_delete_can_perform_single_right_rotation(self):
        tree = AvlTree()
        # Insert multiple nodes
        tree.insert(15)
        tree.insert(10)
        tree.insert(20)
        tree.insert(5)
        # Verify current root
        assert tree.root.data == 15
        # remove value that will cause right rotation
        tree.delete(20)
        # verify right rotation occurred
        assert tree.root.data == 10
        assert tree.root.left.data == 5
        assert tree.root.right.data == 15


    def test_delete_can_perform_double_right_left_rotation(self):
        tree = AvlTree()
        # Insert multiple nodes
        tree.insert(5)
        tree.insert(3)
        tree.insert(15)
        tree.insert(10)
        # Verify current root
        assert tree.root.data == 5
        # remove value that will cause right left rotation
        tree.delete(3)
        # verify right left rotation occurred
        assert tree.root.data == 10
        assert tree.root.left.data == 5
        assert tree.root.right.data == 15


    def test_delete_can_perform_double_left_right_rotation(self):
        tree = AvlTree()
        # Insert multiple nodes
        tree.insert(15)
        tree.insert(5)
        tree.insert(20)
        tree.insert(10)
        # Verify current root
        assert tree.root.data == 15
        # remove value that will cause left right rotation
        tree.delete(20)
        # verify left right rotation occurred
        assert tree.root.data == 10
        assert tree.root.left.data == 5
        assert tree.root.right.data == 15
    

    def test_search(self):
        tree = AvlTree()
        tree.insert(5)
        tree.insert(10)
        tree.insert(100)
        tree.insert(3)
        # Verify search for all numbers
        assert tree.search(5) is True
        assert tree.search(100) is True
        assert tree.search(10) is True
        assert tree.search(3) is True
        assert tree.search(1) is False
        assert tree.search(27) is False



if __name__ == '__main__':
    unittest.main()