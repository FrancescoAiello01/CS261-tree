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
        bst.insert(bst, child)
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
        bst.insert(bst, child)
        bst.insert(bst, child_two)
        bst.insert(bst, child_three)
        bst.insert(bst, child_four)
        self.assertEqual(child, bst.right)
        self.assertEqual(child_two, child.right)
        self.assertEqual(child_three, bst.left)
        self.assertEqual(child_four, child_three.left)


if __name__ == '__main__':
    unittest.main()
