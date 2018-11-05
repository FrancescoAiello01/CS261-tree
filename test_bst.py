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




if __name__ == '__main__':
    unittest.main()
