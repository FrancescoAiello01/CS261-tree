# Run me with 'python -m unittest test_bst'

import unittest
from bst import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    """
    Initialization
    """

    def test_instantiation(self):
        """
        A BinarySearchTree exists
        """
        try:
            BinarySearchTree()
        except NameError:
            self.fail("Could not instantiate BinarySearchTree")

    def test_instantiation_with_value(self):
        test_value = "FAKE"
        bst = BinarySearchTree("FAKE")
        self.assertEqual(test_value, bst.value)

    def test_has_left_and_right_initially_none(self):
        bst = BinarySearchTree()
        self.assertEqual(None, bst.left)
        self.assertEqual(None, bst.right)

    """
    Insert with only the root
    """
    def test_insertion_smaller_values_as_left(self):
        bst = BinarySearchTree(50)
        child = BinarySearchTree(25)
        bst.insert(child)
        self.assertEqual(child, bst.left)

    """
    Insert with four values from root
    """
    def test_insert_smaller_and_bigger_values(self):
        bst = BinarySearchTree(50)
        child = BinarySearchTree(56)
        child_two = BinarySearchTree(61)
        child_three = BinarySearchTree(39)
        child_four = BinarySearchTree(30)
        bst.insert(child)
        bst.insert(child_two)
        bst.insert(child_three)
        bst.insert(child_four)
        self.assertEqual(child, bst.right)
        self.assertEqual(child_two, child.right)
        self.assertEqual(child_three, bst.left)
        self.assertEqual(child_four, child_three.left)

    """
    Find value in tree with four leaf nodes
    """
    def test_find_value_in_tree_with_four_leaf_nodes(self):
        searchee = 53
        bst = BinarySearchTree(50)
        child = BinarySearchTree(56)
        child_two = BinarySearchTree(61)
        child_three = BinarySearchTree(53)
        child_four = BinarySearchTree(30)
        child_five = BinarySearchTree(26)
        child_six = BinarySearchTree(31)
        bst.insert(child)
        bst.insert(child_two)
        bst.insert(child_three)
        bst.insert(child_four)
        bst.insert(child_five)
        bst.insert(child_six)
        self.assertEqual(True, bst.find(searchee))
        self.assertEqual(False, bst.find(1))

    """
    In-order traversal test
    """
    def test_in_order_traversal(self):
        bst = BinarySearchTree(50)
        for i in range(5, 80, 10):
            bst.insert(BinarySearchTree(i))
        expected_list = [5, 15, 25, 35, 45, 50, 55, 65, 75]
        observed_list = []
        bst.in_order_traversal(lambda value: observed_list.append(value))
        self.assertEqual(expected_list, observed_list)

    """
    Pre-order traversal test
    """
    def test_pre_order_traversal(self):
        bst = BinarySearchTree(50)
        for i in range(5, 80, 10):
            bst.insert(BinarySearchTree(i))
        expected_list = [50, 5, 15, 25, 35, 45, 55, 65, 75]
        observed_list = []
        bst.pre_order_traversal(lambda value: observed_list.append(value))
        self.assertEqual(expected_list, observed_list)

    """
    Post-order traversal test
    """
    def test_post_order_traversal(self):
        bst = BinarySearchTree(50)
        for i in range(5, 80, 10):
            bst.insert(BinarySearchTree(i))
        expected_list = [45, 35, 25, 15, 5, 75, 65, 55, 50]
        observed_list = []
        bst.post_order_traversal(lambda value: observed_list.append(value))
        self.assertEqual(expected_list, observed_list)

    """
    Delete function test
    """
    def test_delete_function(self):
        bst = BinarySearchTree(50)
        for i in range(5, 80, 10):
            bst.insert(BinarySearchTree(i))
        bst.delete(5)
        self.assertEqual(bst.left.value, 15)

    """
    Delete with two children
    """
    def test_delete_function_with_two_children(self):
        bst = BinarySearchTree(25)
        nodes = [15,50,10,22,35,70,4,12,18,24,31,44,66,90]
        for val in nodes:
            bst.insert(BinarySearchTree(val))
        self.assertEqual(bst.find(50), True)
        bst.delete(50)
        self.assertEqual(bst.find(50), False)

    """
    Delete a value not in the tree
    """
    def test_delete_value_not_in_tree(self):
         bst = BinarySearchTree(25)
         nodes = [15,50,10,22,35,70,4,12,18,24,31,44,66,90]
         for val in nodes:
             bst.insert(BinarySearchTree(val))
         bst.delete(500)

if __name__ == '__main__':
    unittest.main()
