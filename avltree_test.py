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
        tree.insert("cat", "meows")
        # Verify root node
        assert isinstance(tree.root, AvlTreeNode)
        assert tree.root.word == "cat"
        assert tree.root.next_words == ["meows"]
        assert tree.root.left is None
        assert tree.root.right is None


    def test_insert_with_multiple_nodes(self):
        tree = AvlTree()
        # Insert new node that starts from root node
        tree.insert("cat", "meows")
        # Verify root node
        assert isinstance(tree.root, AvlTreeNode)
        assert tree.root.word == "cat"
        assert tree.root.next_words == ["meows"]
        assert tree.root.left is None
        assert tree.root.right is None
        # Insert new node is larger than the root
        tree.insert("dog", "barks")
        # Verify new node "dog"
        assert tree.root.right is not None
        assert tree.root.right.word == "dog"
        assert tree.root.right.next_words == ["barks"]
        assert isinstance(tree.root.right, AvlTreeNode)
        assert tree.root.left is None
        # Insert new node is smaller than the root
        tree.insert("bat", "squeaks")
        # Verify new node 3
        assert tree.root.left is not None
        assert tree.root.left.word == "bat"
        assert tree.root.left.next_words == ["squeaks"]
        assert isinstance(tree.root.left, AvlTreeNode)
        

    def test_insert_can_perform_single_left_rotation(self):
        tree = AvlTree()
        # insert new node
        tree.insert("cat", "meows")
        # Verify current root
        assert tree.root.word == "cat"
        assert tree.root.next_words == ["meows"]
        # insert values that will cause left rotation
        tree.insert("dog", "barks")
        tree.insert("frog", "croaks")
        # verify left rotation occurred
        assert tree.root.word == "dog"
        assert tree.root.left.word == "cat"
        assert tree.root.right.word == "frog"
    
    
    def test_insert_can_perform_single_right_rotation(self):
        tree = AvlTree()
        # insert new node
        tree.insert("frog", "croak")
        # Verify current root
        assert tree.root.word == "frog"
        # insert values that will cause right rotation
        tree.insert("dog", "barks")
        tree.insert("cat", "meows")
        # verify right rotation occurred
        assert tree.root.word == "dog"
        assert tree.root.left.word == "cat"
        assert tree.root.right.word == "frog"
    
    
    def test_insert_can_perform_double_right_left_rotation(self):
        tree = AvlTree()
        # insert new node
        tree.insert("cat", "meows")
        # Verify current root
        assert tree.root.word == "cat"
        # insert values that will cause right left rotation
        tree.insert("frog", "croak")
        tree.insert("dog", "barks")
        # verify right left rotation occurred
        assert tree.root.word == "dog"
        assert tree.root.left.word == "cat"
        assert tree.root.right.word == "frog"


    def test_insert_can_perform_double_left_right_rotation(self):
        tree = AvlTree()
        # insert new node
        tree.insert("frog", "croak")
        # Verify current root
        assert tree.root.word == "frog"
        # insert values that will cause left right rotation
        tree.insert("cat", "meows")
        tree.insert("dog", "barks")
        # verify left right rotation occurred
        assert tree.root.word == "dog"
        assert tree.root.left.word == "cat"
        assert tree.root.right.word == "frog"


    def test_delete(self):
        tree = AvlTree()
        # insert new node
        tree.insert("cat", "meows")
        # Verify root node
        assert tree.root.word == "cat"
        # delete node
        tree.delete("cat")
        assert tree.root is None


    def test_delete_with_multiple_nodes(self):
        tree = AvlTree()
        # Insert multiple nodes
        tree.insert("cat", "meows")
        tree.insert("dog", "barks")
        # Verify root node
        assert tree.root.word == "cat"
        assert tree.root.right.word == "dog"
        # delete node
        tree.delete("cat")
        assert tree.root.word == "dog"
        assert tree.root.right is None
        assert tree.search("cat") is False


    def test_delete_can_perform_single_left_rotation(self):
        tree = AvlTree()
        # Insert multiple nodes
        tree.insert("cat", "meows")
        tree.insert("bat", "squeaks")
        tree.insert("dog", "barks")
        tree.insert("frog", "croak")
        # Verify current root
        assert tree.root.word == "cat"
        # remove value that will cause left rotation
        tree.delete("bat")
        # verify left rotation occurred
        assert tree.root.word == "dog"
        assert tree.root.left.word == "cat"
        assert tree.root.right.word == "frog"


    def test_delete_can_perform_single_right_rotation(self):
        tree = AvlTree()
        # Insert multiple nodes
        tree.insert("frog", "croak")
        tree.insert("dog", "barks")
        tree.insert("lamb", "bleats")
        tree.insert("cat", "meows")
        # Verify current root
        assert tree.root.word == "frog"
        # remove value that will cause right rotation
        tree.delete("lamb")
        # verify right rotation occurred
        assert tree.root.word == "dog"
        assert tree.root.left.word == "cat"
        assert tree.root.right.word == "frog"


    def test_delete_can_perform_double_right_left_rotation(self):
        tree = AvlTree()
        # Insert multiple nodes
        tree.insert("cat", "meows")
        tree.insert("bat", "sqeaks")
        tree.insert("frog", "croaks")
        tree.insert("dog", "barks")
        # Verify current root
        assert tree.root.word == "cat"
        # remove value that will cause right left rotation
        tree.delete("bat")
        # verify right left rotation occurred
        assert tree.root.word == "dog"
        assert tree.root.left.word == "cat"
        assert tree.root.right.word == "frog"


    def test_delete_can_perform_double_left_right_rotation(self):
        tree = AvlTree()
        # Insert multiple nodes
        tree.insert("frog", "croaks")
        tree.insert("cat", "meows")
        tree.insert("lamb", "bleats")
        tree.insert("dog", "barks")
        # Verify current root
        assert tree.root.word == "frog"
        # remove value that will cause left right rotation
        tree.delete("lamb")
        # verify left right rotation occurred
        assert tree.root.word == "dog"
        assert tree.root.left.word == "cat"
        assert tree.root.right.word == "frog"
    

    def test_search(self):
        tree = AvlTree()
        tree.insert("cat", "meows")
        tree.insert("dog", "barks")
        tree.insert("lamb", "bleats")
        # Verify search for all numbers
        assert isinstance(tree.search("cat"), AvlTreeNode)
        assert isinstance(tree.search("lamb"), AvlTreeNode)
        assert isinstance(tree.search("dog"), AvlTreeNode)
        assert tree.search("giraffe") is False
        assert tree.search("otter") is False
        assert tree.search("squid") is False



if __name__ == '__main__':
    unittest.main()