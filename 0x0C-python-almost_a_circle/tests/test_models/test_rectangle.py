#!/usr/bin/python3
"""This module defines test cases for the Rectangle class"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def test_init(self):
        """Test initialization"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_area(self):
        """Test area method"""
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.area(), 12)

    def test_display(self):
        """Test display method (no real test, just for coverage)"""
        r3 = Rectangle(2, 2)
        r3.display()

    # Add more tests as needed


if __name__ == '__main__':
    unittest.main()
