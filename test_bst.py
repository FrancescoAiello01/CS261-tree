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


if __name__ == '__main__':
    unittest.main()
