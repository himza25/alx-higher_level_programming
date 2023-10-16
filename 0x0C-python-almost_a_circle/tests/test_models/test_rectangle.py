#!/usr/bin/python3
"""This module defines tests for class Rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests to check the functionality of Rectangle class"""

    def test_init(self):
        """Test for working __init__ method"""
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)

    def test_area(self):
        """Test for area method"""
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.area(), 200)

    def test_display(self):
        """Test for display method"""
        pass  # Implement this test

    def test_str(self):
        """Test for __str__ method"""
        r1 = Rectangle(10, 20, 1, 1, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/1 - 10/20")

    def test_update(self):
        """Test for update method"""
        r1 = Rectangle(10, 20, 1, 1, 1)
        r1.update(2, 3, 4, 5, 6)
        self.assertEqual(str(r1), "[Rectangle] (2) 5/6 - 3/4")


if __name__ == "__main__":
    unittest.main()
