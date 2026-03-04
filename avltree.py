#!python3

from avltreenode import AvlTreeNode


class AvlTree:
    """AvlTree: A self-balancing avl tree that stores words with efficient
    methods to insert an element into the tree, delete an element from the tree, 
    search for an element within the tree, and perform left and right rotations.
    """

    def __init__(self):
        """Initialize this avl tree."""
        self.root = None

    def insert(self, word, next_word):
        """Update the root of the Avl tree with the new tree node inserted."""
        if next_word is None:
            return self.root
        self.root = self._recursive_insert(word, next_word, self.root)
        return self.root
        
    def _recursive_insert(self, word, next_word, current_node):
        """Recursively find the insertion point for the new node and rotate
        the nodes if needed, update the subtrees."""
        # if there is no current node, return the new node
        if current_node is None:
            node = AvlTreeNode(word)
            node.next_words.append(next_word)
            return node
        
        # If word already exists, append and stop
        if word == current_node.word:
            current_node.next_words.append(next_word)
            return current_node
    
        # if the new node's word is bigger than our current node's word
        if word > current_node.word:
            # call the recursive insertion function on the right node
            current_node.right = self._recursive_insert(word, next_word, current_node.right)
        # else call the recursive insertion function on the left node
        else:
            current_node.left = self._recursive_insert(word, next_word, current_node.left)
        
        # update the height of the current node based on its subtrees
        left_height = self._calculate_node_height(current_node.left)
        right_height = self._calculate_node_height(current_node.right)
        current_node.height = max(left_height, right_height) + 1
        
        # use the balance factor
        balance_factor = self._calculate_balance_factor(current_node)
        
        # to decide if we need to do a single right rotation
        if balance_factor > 1 and word < current_node.left.word:
            return self._rotate_right(current_node)
        # a left right double rotation
        elif balance_factor > 1 and word > current_node.left.word:
            current_node.left = self._rotate_left(current_node.left)
            return self._rotate_right(current_node)
        # a sigle left rotation
        elif balance_factor < -1 and word > current_node.right.word: 
            return self._rotate_left(current_node)
        # a right left double rotation
        elif balance_factor < -1 and word < current_node.right.word: 
            current_node.right = self._rotate_right(current_node.right)
            return self._rotate_left(current_node)
        
        return current_node
    
    
    def delete(self, word):
        """Update the root of the Avl tree with the tree node removed."""
        self.root = self._recursive_delete(word, self.root)
        return self.root
    
    def _recursive_delete(self, word, current_node):
        """Recursively find the node to remove and rotate the nodes if needed, update the subtrees."""
        # if there is no current node, return none
        if current_node is None:
            return current_node
        
        # if the removed node's word is bigger than our current node's word
        if word > current_node.word:
            # call the recursive delete function on the right node
            current_node.right = self._recursive_delete(word, current_node.right)
        # else call the recursive delete function on the left node
        elif word < current_node.word:
            current_node.left = self._recursive_delete(word, current_node.left)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            else:
                min_node = self._find_min_value_in_subtree(current_node.right)
                current_node.word = min_node.word
                current_node.next_words = min_node.next_words
                current_node.right = self._recursive_delete(min_node.word, current_node.right)
        
        # update the height of the current node based on its subtrees
        left_height = self._calculate_node_height(current_node.left)
        right_height = self._calculate_node_height(current_node.right)
        current_node.height = max(left_height, right_height) + 1
        
        # use the balance factor
        balance_factor = self._calculate_balance_factor(current_node)
        
        # to decide if we need to do a single right rotation
        if balance_factor > 1 and self._calculate_balance_factor(current_node.left) >= 0:
            return self._rotate_right(current_node)
        # a left right double rotation
        elif balance_factor > 1 and self._calculate_balance_factor(current_node.left) < 0:
            current_node.left = self._rotate_left(current_node.left)
            return self._rotate_right(current_node)
        # a sigle left rotation
        elif balance_factor < -1 and self._calculate_balance_factor(current_node.right) <= 0: 
            return self._rotate_left(current_node)
        # a right left double rotation
        elif balance_factor < -1 and self._calculate_balance_factor(current_node.right) > 0: 
            current_node.right = self._rotate_right(current_node.right)
            return self._rotate_left(current_node)
        
        return current_node
    
    def _find_min_value_in_subtree(self, node):
        '''Find the node with the smallest value in the subtree.'''
        current_node = node
        
        while current_node.left is not None:
            current_node = current_node.left
        
        return current_node
    
    def search(self, word):
        """Traverse the tree and look for a node with a word value of the provided value.
        If a node is found with that value, return True, else return False."""
        # make sure there is a root
        if self.root is None:
            return False
        
        current_node = self.root
        
        # loop until we reach the bottom of the tree
        while current_node is not None:
            # return true if the node is the node we're looking for
            if current_node.word == word:
                return current_node
            # move to the right node of the current node if the node we're looking for is
            # larger than the current node
            elif word > current_node.word:
                current_node = current_node.right
            # move to the left node of the current node if the node we're looking for is
            # smaller than the current node
            else:
                current_node = current_node.left
        
        # return false if we didn't find a node with the right word
        return False
    
    
    def _rotate_right(self, node):
        '''Rotate the nodes to the right.'''
        new_subtree_root = node.left
        node.left = new_subtree_root.right
        new_subtree_root.right = node
        
        node_left_height = self._calculate_node_height(node.left)
        node_right_height = self._calculate_node_height(node.right)
        node.height = max(node_left_height, node_right_height) + 1
        
        new_node_left_height = self._calculate_node_height(new_subtree_root.left)
        new_node_right_height = self._calculate_node_height(new_subtree_root.right)
        new_subtree_root.height = max(new_node_right_height, new_node_left_height) + 1
        return new_subtree_root
    
    
    def _rotate_left(self, node):
        '''Rotate the nodes to the left.'''
        new_subtree_root = node.right
        node.right = new_subtree_root.left
        new_subtree_root.left = node
        
        node_left_height = self._calculate_node_height(node.left)
        node_right_height = self._calculate_node_height(node.right)
        node.height = max(node_left_height, node_right_height) + 1
        
        new_node_right_height = self._calculate_node_height(new_subtree_root.right)
        new_node_left_height = self._calculate_node_height(new_subtree_root.left)
        new_subtree_root.height = max(new_node_left_height, new_node_right_height) + 1
        
        return new_subtree_root
    
    
    def _calculate_node_height(self, node):
        '''Determine the height of the node if it exists.'''
        if node is None:
            return -1
        else:
            return node.height
        
    
    def _calculate_balance_factor(self, node):
        '''Calculate the balance factor of the node based on its left and right nodes.'''
        left_height = self._calculate_node_height(node.left)
        right_height = self._calculate_node_height(node.right)
        return left_height - right_height