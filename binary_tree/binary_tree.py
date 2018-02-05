class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return True if self.right == None and self.left == None else False

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return True if self.right != None or self.left != None else False

    def get_height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""
        if self.is_leaf():
            return 0
        if self.left == None:
            return 1 + max(0, self.right.get_height())
        elif self.right == None:
            return 1 + max(self.left.get_height(), 0)
        else:
            return max(self.left.get_height(), self.right.get_height()) + 1



class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""
        if self.is_empty():
            return 0
        return self.root.get_height()


    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        return node.data if node != None else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Handle the case where the tree is empty
        if self.is_empty():
            self.root = BinaryTreeNode(item)
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node(item)
        if item < parent.data:
            parent.left = BinaryTreeNode(item)
        elif item > parent.data:
            parent.right = BinaryTreeNode(item)
        self.size += 1

    def _find_node(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            if item == node.data:
                # Return the found node
                return node
            elif item < node.data:
                node = node.left
            elif item > node.data:
                node = node.right
        # Not found
        return None

    def _find_parent_node(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            if item == node.data:
                # Return the parent of the found node
                return parent
            elif item < node.data:
                parent = node
                node = node.left
            elif item > node.data:
                parent = node
                node = node.right
        # Not found
        return parent

    def delete(self, item):
        node_to_delete = self._find_node(item)
        if node_to_delete != None:
            self.size -= 1
            parent_node = self._find_parent_node(node_to_delete.data)
            if node_to_delete.right != None and node_to_delete.left != None:
                self._delete_branch_node(node_to_delete, parent_node, 2)
            elif node_to_delete.is_leaf():
                self._delete_leaf_node(node_to_delete, parent_node)
            else:
                self._delete_branch_node(node_to_delete, parent_node)
    
    def _delete_leaf_node(self, node, parent):
        if node.data > parent.data:
            parent.right = None
            return
        
        parent.left = None
        
    def _delete_branch_node(self, node, parent, children=1):
        assert 0 < children < 3
        direction = 'right' if parent.right == node else 'left'
        if children == 1:
            node_child = node.right if node.right != None else node.left
            if direction == 'right':
                parent.right = node_child
            else:
                parent.left = node_child
        else:
            successor = self._find_successor(node)
            successor.left = node.left
            if successor.is_leaf() and node.right != successor:
                successor.right = node.right
            if direction == 'right':
                parent.right = successor
            else:
                parent.left = successor

    def _find_successor(self, node):
        node = node.right
        while node.left != None:
            node = node.left
        return node



    # This space intentionally left blank (please do not delete this comment)

    # def items_in_order(self):
    #     """Return an in-order list of all items in this binary search tree."""
    #     items = []
    #     if not self.is_empty():
    #         # Traverse tree in-order from root, appending each node's item
    #         self._traverse_in_order_recursive(self.root, items.append):
    #     # Return in-order list of all items in tree
    #     return items

    # def _traverse_in_order_recursive(self, node, visit):
    #     """Traverse this binary tree with recursive in-order traversal (DFS).
    #     Start at the given node and visit each node with the given function.
    #     TODO: Running time: ??? Why and under what conditions?
    #     TODO: Memory usage: ??? Why and under what conditions?"""
    #     # TODO: Traverse left subtree, if it exists
    #     ...
    #     # TODO: Visit this node's data with given function
    #     ...
    #     # TODO: Traverse right subtree, if it exists
    #     ...

    # def _traverse_in_order_iterative(self, node, visit):
    #     """Traverse this binary tree with iterative in-order traversal (DFS).
    #     Start at the given node and visit each node with the given function.
    #     TODO: Running time: ??? Why and under what conditions?
    #     TODO: Memory usage: ??? Why and under what conditions?"""
    #     # TODO: Traverse in-order without using recursion (stretch challenge)

    # def items_pre_order(self):
    #     """Return a pre-order list of all items in this binary search tree."""
    #     items = []
    #     if not self.is_empty():
    #         # Traverse tree pre-order from root, appending each node's item
    #         self._traverse_pre_order_recursive(self.root, items.append):
    #     # Return pre-order list of all items in tree
    #     return items

    # def _traverse_pre_order_recursive(self, node, visit):
    #     """Traverse this binary tree with recursive pre-order traversal (DFS).
    #     Start at the given node and visit each node with the given function.
    #     TODO: Running time: ??? Why and under what conditions?
    #     TODO: Memory usage: ??? Why and under what conditions?"""
    #     # TODO: Visit this node's data with given function
    #     ...
    #     # TODO: Traverse left subtree, if it exists
    #     ...
    #     # TODO: Traverse right subtree, if it exists
    #     ...

    # def _traverse_pre_order_iterative(self, node, visit):
    #     """Traverse this binary tree with iterative pre-order traversal (DFS).
    #     Start at the given node and visit each node with the given function.
    #     TODO: Running time: ??? Why and under what conditions?
    #     TODO: Memory usage: ??? Why and under what conditions?"""
    #     # TODO: Traverse pre-order without using recursion (stretch challenge)

    # def items_post_order(self):
    #     """Return a post-order list of all items in this binary search tree."""
    #     items = []
    #     if not self.is_empty():
    #         # Traverse tree post-order from root, appending each node's item
    #         self._traverse_post_order_recursive(self.root, items.append):
    #     # Return post-order list of all items in tree
    #     return items

    # def _traverse_post_order_recursive(self, node, visit):
    #     """Traverse this binary tree with recursive post-order traversal (DFS).
    #     Start at the given node and visit each node with the given function.
    #     TODO: Running time: ??? Why and under what conditions?
    #     TODO: Memory usage: ??? Why and under what conditions?"""
    #     # TODO: Traverse left subtree, if it exists
    #     ...
    #     # TODO: Traverse right subtree, if it exists
    #     ...
    #     # TODO: Visit this node's data with given function
    #     ...

    # def _traverse_post_order_iterative(self, node, visit):
    #     """Traverse this binary tree with iterative post-order traversal (DFS).
    #     Start at the given node and visit each node with the given function.
    #     TODO: Running time: ??? Why and under what conditions?
    #     TODO: Memory usage: ??? Why and under what conditions?"""
    #     # TODO: Traverse post-order without using recursion (stretch challenge)

    # def items_level_order(self):
    #     """Return a level-order list of all items in this binary search tree."""
    #     items = []
    #     if not self.is_empty():
    #         # Traverse tree level-order from root, appending each node's item
    #         self._traverse_level_order_iterative(self.root, items.append):
    #     # Return level-order list of all items in tree
    #     return items

    # def _traverse_level_order_iterative(self, start_node, visit):
    #     """Traverse this binary tree with iterative level-order traversal (BFS).
    #     Start at the given node and visit each node with the given function.
    #     TODO: Running time: ??? Why and under what conditions?
    #     TODO: Memory usage: ??? Why and under what conditions?"""
    #     # TODO: Create queue to store nodes not yet traversed in level-order
    #     queue = ...
    #     # TODO: Enqueue given starting node
    #     ...
    #     # TODO: Loop until queue is empty
    #     while ...:
    #         # TODO: Dequeue node at front of queue
    #         node = ...
    #         # TODO: Visit this node's data with given function
    #         ...
    #         # TODO: Enqueue this node's left child, if it exists
    #         ...
    #         # TODO: Enqueue this node's right child, if it exists
    #         ...


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    # test_binary_search_tree()
    def test_delete_7_items():
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        assert tree.contains(1) == True
        tree.delete(1)
        assert tree.contains(1) == False

    test_delete_7_items()