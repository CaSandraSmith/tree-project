#!python3


class AvlTreeNode:
    """AvlTreeNode: A node for use in a AVL tree that stores its data
    and its left and right nodes"""

    def __init__(self, word):
        """Initialize this avl tree node with the given word value, 
        an empty list for its next words, None for its left and right 
        nodes, and a height of 0."""
        self.word = word
        self.next_words = []
        self.left = None
        self.right = None
        self.height = 0

    def __repr__(self):
        """Return a code representation of this AVL tree node."""
        return f'AvlTreeNode({self.word!r})'

    def __str__(self):
        """Return a string view of this AVL tree node."""
        return f'({self.word})'