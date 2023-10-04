#!/usr/bin/python3
"""Unittest for max_integer([..])
This module contains unittests to test the function `max_integer(list=[])`.
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines a class for testing the function `max_integer(list=[])`."""

    def test_max_integer(self):
        """Tests normal cases."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        """Tests when the list is empty."""
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """Tests when the list contains a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_string_list(self):
        """Tests when the list contains strings."""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_mixed_list(self):
        """Tests when the list contains mixed types."""
        with self.assertRaises(TypeError):
            max_integer([1, "string", 3, 4])


if __name__ == '__main__':
    unittest.main()
