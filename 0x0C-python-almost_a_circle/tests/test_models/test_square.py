#!/usr/bin/python3
"""This module defines tests for class Square"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests to check the functionality of Square class"""

    def test_init(self):
        """Test for working __init__ method"""
        s1 = Square(10)
        self.assertEqual(s1.size, 10)

    def test_str(self):
        """Test for __str__ method"""
        s1 = Square(10, 1, 1, 1)
        self.assertEqual(str(s1), "[Square] (1) 1/1 - 10")

    def test_update(self):
        """Test for update method"""
        s1 = Square(10, 1, 1, 1)
        s1.update(2, 3, 4, 5)
        self.assertEqual(str(s1), "[Square] (2) 4/5 - 3")


if __name__ == "__main__":
    unittest.main()
