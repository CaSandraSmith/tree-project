#!python3


class AvlTreeNode:
    """AvlTreeNode: A node for use in a AVL tree that stores its data
    and its left and right nodes"""

    def __init__(self, data):
        """Initialize this avl tree node with the given data value, 
        None for its left and right nodes, and a height of 0."""
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def __repr__(self):
        """Return a code representation of this AVL tree node."""
        return f'AvlTreeNode({self.data!r})'

    def __str__(self):
        """Return a string view of this AVL tree node."""
        return f'({self.data})'