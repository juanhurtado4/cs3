from binary_tree import BinarySearchTree, BinaryTreeNode
import unittest
import pytest

class BinaryTreeNodeTest(unittest.TestCase):

    def test_init(self):
        data = 123
        node = BinaryTreeNode(data)
        assert node.data is data
        assert node.left is None
        assert node.right is None

    def test_is_leaf(self):
        # Create node with no children
        node = BinaryTreeNode(2)
        assert node.is_leaf() is True
        # Attach left child node
        node.left = BinaryTreeNode(1)
        assert node.is_leaf() is False
        # Attach right child node
        node.right = BinaryTreeNode(3)
        assert node.is_leaf() is False
        # Detach left child node
        node.left = None
        assert node.is_leaf() is False
        # Detach right child node
        node.right = None
        assert node.is_leaf() is True

    def test_is_branch(self):
        # Create node with no children
        node = BinaryTreeNode(2)
        assert node.is_branch() is False
        # Attach left child node
        node.left = BinaryTreeNode(1)
        assert node.is_branch() is True
        # Attach right child node
        node.right = BinaryTreeNode(3)
        assert node.is_branch() is True
        # Detach left child node
        node.left = None
        assert node.is_branch() is True
        # Detach right child node
        node.right = None
        assert node.is_branch() is False
    
    def test_height(self):
        # Create node with no children
        root_node = BinaryTreeNode(10)
        child_node4 = BinaryTreeNode(4)
        child_node3 = BinaryTreeNode(3)
        child_node7 = BinaryTreeNode(7)
        child_node20 = BinaryTreeNode(20)
        child_node15 = BinaryTreeNode(15)
        child_node22 = BinaryTreeNode(22)
        child_node21 = BinaryTreeNode(21)
        root_node.left = child_node4
        root_node.right = child_node20
        child_node4.left = child_node3
        child_node4.right = child_node7
        child_node20.left = child_node15
        child_node20.right = child_node22
        child_node22.left = child_node21
        '''
        BST Visualization:
                 10
               /    \
              4      20
             / \    /   \
            3   7  15    22
                        /
                       21  
        '''
        assert root_node.get_height() == 3
        assert child_node20.get_height() == 2
        assert child_node4.get_height() == 1
        assert child_node22.get_height() == 1
        assert child_node3.get_height() == 0
        assert child_node7.get_height() == 0
        assert child_node15.get_height() == 0
        assert child_node21.get_height() == 0
        
        


class BinarySearchTreeTest(unittest.TestCase):

    def test_init(self):
        tree = BinarySearchTree()
        assert tree.root is None
        assert tree.size == 0
        assert tree.is_empty() is True

    def test_init_with_list(self):
        tree = BinarySearchTree([2, 1, 3])
        assert tree.root.data == 2
        assert tree.root.left.data == 1
        assert tree.root.right.data == 3
        assert tree.size == 3
        assert tree.is_empty() is False

    def test_init_with_list_of_strings(self):
        tree = BinarySearchTree(['B', 'A', 'C'])
        assert tree.root.data == 'B'
        assert tree.root.left.data == 'A'
        assert tree.root.right.data == 'C'
        assert tree.size == 3
        assert tree.is_empty() is False

    def test_init_with_list_of_tuples(self):
        tree = BinarySearchTree([(2, 'B'), (1, 'A'), (3, 'C')])
        assert tree.root.data == (2, 'B')
        assert tree.root.left.data == (1, 'A')
        assert tree.root.right.data == (3, 'C')
        assert tree.size == 3
        assert tree.is_empty() is False

    def test_size(self):
        tree = BinarySearchTree()
        assert tree.size == 0
        tree.insert('B')
        assert tree.size == 1
        tree.insert('A')
        assert tree.size == 2
        tree.insert('C')
        assert tree.size == 3
    
    def test_height(self):
        tree = BinarySearchTree()
        '''
        BST Visualization:
                 D
               /   \
              A     H
               \     \
                B     K
                     /
                    I
        '''
        assert tree.height() == 0
        tree.insert('D')
        # import pdb; pdb.set_trace()
        assert tree.height() == 0
        tree.insert('A')
        assert tree.height() == 1
        tree.insert('B')
        assert tree.height() == 2
        tree.insert('H')
        assert tree.height() == 2
        tree.insert('K')
        assert tree.height() == 2
        tree.insert('I')
        assert tree.height() == 3

    def test_search_with_3_items(self):
        # Create a complete binary search tree of 3 items in level-order
        items = [2, 1, 3]
        tree = BinarySearchTree(items)
        assert tree.search(1) == 1
        assert tree.search(2) == 2
        assert tree.search(3) == 3
        assert tree.search(4) is None

    def test_search_with_7_items(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        for item in items:
            assert tree.search(item) == item
        assert tree.search(8) is None

    def test_search_with_3_strings(self):
        # Create a complete binary search tree of 3 items in level-order
        items = ['B', 'A', 'C']
        tree = BinarySearchTree(items)
        assert tree.search('A') == 'A'
        assert tree.search('B') == 'B'
        assert tree.search('C') == 'C'
        assert tree.search('D') is None

    def test_search_with_7_strings(self):
        # Create a complete binary search tree of 7 items in level-order
        items = ['D', 'B', 'F', 'A', 'C', 'E', 'G']
        tree = BinarySearchTree(items)
        for item in items:
            assert tree.search(item) == item
        assert tree.search('H') is None

    def test_insert_with_3_items(self):
        # Create a complete binary search tree of 3 items in level-order
        tree = BinarySearchTree()
        tree.insert(2)
        assert tree.root.data == 2
        assert tree.root.left is None
        assert tree.root.right is None
        tree.insert(1)
        assert tree.root.data == 2
        assert tree.root.left.data == 1
        assert tree.root.right is None
        tree.insert(3)
        assert tree.root.data == 2
        assert tree.root.left.data == 1
        assert tree.root.right.data == 3

    def test_insert_with_7_items(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree()
        for item in items:
            tree.insert(item)
        assert tree.root.data == 4
        assert tree.root.left.data == 2
        assert tree.root.right.data == 6
        assert tree.root.left.left.data == 1
        assert tree.root.left.right.data == 3
        assert tree.root.right.left.data == 5
        assert tree.root.right.right.data == 7

    def test_delete_leaf_nodes(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        assert tree.contains(1) == True
        tree.delete(1)
        assert tree.contains(1) == False
        # Check that deepest left leaf on left side of tree is none
        assert tree.root.left.left == None

        assert tree.contains(3) == True
        tree.delete(3)
        assert tree.contains(3) == False
        # Check that deepest right leaf on left side of tree is none
        assert tree.root.left.right == None
        assert tree.size == 5

        tree2 = BinarySearchTree([1])
        tree2.delete(1)
        assert tree2.size == 0
        assert tree2.root == None
        assert tree2.contains(1) == False


    def test_delete_branch_nodes_with_one_child(self):
        items = [4, 2, 6, 3, 5]
        tree = BinarySearchTree(items)
        assert tree.contains(2) == True
        tree.delete(2)
        assert tree.contains(2) == False
        # Check for the correct node to take place of the deleted node
        assert tree.root.left.data == 3
        assert tree.root.left.is_leaf() == True
        assert tree.size == 4

        assert tree.contains(6) == True
        tree.delete(6)
        assert tree.contains(6) == False
        # Check for the correct node to take place of the deleted node
        assert tree.root.right.data == 5
        assert tree.root.right.is_leaf() == True
        assert tree.size == 3
        
    def test_delete_branch_nodes_with_2_children(self):
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        assert tree.contains(2) == True
        tree.delete(2)
        assert tree.contains(2) == False
        # Check for the correct node to take place of the deleted node
        assert tree.root.left.data == 3
        assert tree.root.left.right == None
        assert tree.root.left.left.data == 1
        assert tree.size == 6

        assert tree.contains(6) == True
        tree.delete(6)
        assert tree.contains(6) == False
        # Check for the correct node to take place of the deleted node
        assert tree.root.right.data == 7
        assert tree.root.right.right == None
        assert tree.root.right.left.data == 5
        assert tree.size == 5

        # Delete root node on a full tree where successor is leaf
        items2 = [4, 2, 6, 1, 3, 5, 7]        
        tree2 = BinarySearchTree(items2)
        tree2.delete(4)
        assert tree2.root.data == 5
        assert tree2.size == 6

        # Delete root node on a full tree where successor has 1 child
        items3 = [4, 2, 7, 1, 3, 5, 6, 8]        
        tree3 = BinarySearchTree(items3)
        assert tree3.size == 8
        # Check that the correct successor is found
        successor = tree3._find_successor(tree3.root)
        # Check that successor has correct child
        assert successor.data == 5
        assert successor.right.data == 6
        assert successor.left == None
        tree3.delete(4)
        # Check if successor took the place of root
        assert tree3.root.data == 5
        # Check left side of tree is intact
        assert tree3.root.left.data == 2
        assert tree3.root.left.left.data == 1
        assert tree3.root.left.right.data == 3
        # Check right side of tree is intact
        assert tree3.root.right.data == 7
        assert tree3.root.right.left.data == 6
        assert tree3.root.right.right.data == 8
        assert tree3.root.right.left.is_leaf() == True
        assert tree3.root.right.right.is_leaf() == True
        assert tree3.size == 7
        

    # This space intentionally left blank (please do not delete this comment)

    def test_items_in_order_with_3_strings(self):
        # Create a complete binary search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = BinarySearchTree(items)
        # Ensure the in-order traversal of tree items is ordered correctly
        assert tree.items_in_order() == ['A', 'B', 'C']

    def test_items_pre_order_with_3_strings(self):
        # Create a complete binary search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = BinarySearchTree(items)
        # Ensure the pre-order traversal of tree items is ordered correctly
        assert tree.items_pre_order() == ['B', 'A', 'C']

    def test_items_post_order_with_3_strings(self):
        # Create a complete binary search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = BinarySearchTree(items)
        # Ensure the post-order traversal of tree items is ordered correctly
        assert tree.items_post_order() == ['A', 'C', 'B']

    def test_items_level_order_with_3_strings(self):
        # Create a complete binary search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = BinarySearchTree(items)
        # Ensure the level-order traversal of tree items is ordered correctly
        assert tree.items_level_order() == ['B', 'A', 'C']

    def test_items_in_order_with_7_numbers(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        # Ensure the in-order traversal of tree items is ordered correctly
        assert tree.items_in_order() == [1, 2, 3, 4, 5, 6, 7]

    def test_items_pre_order_with_7_numbers(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        # Ensure the pre-order traversal of tree items is ordered correctly
        assert tree.items_pre_order() == [4, 2, 1, 3, 6, 5, 7]

    def test_items_post_order_with_7_numbers(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        # Ensure the post-order traversal of tree items is ordered correctly
        assert tree.items_post_order() == [1, 3, 2, 5, 7, 6, 4]

    def test_items_level_order_with_7_numbers(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        # Ensure the level-order traversal of tree items is ordered correctly
        assert tree.items_level_order() == [4, 2, 6, 1, 3, 5, 7]


if __name__ == '__main__':
    unittest.main()