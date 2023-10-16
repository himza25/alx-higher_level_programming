#!/usr/bin/python3
"""This module defines test cases for the Square class"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def test_init(self):
        """Test initialization"""
        s1 = Square(1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)

    def test_size(self):
        """Test the size getter and setter"""
        s2 = Square(2)
        s2.size = 3
        self.assertEqual(s2.size, 3)

    # Add more tests as needed


if __name__ == '__main__':
    unittest.main()
