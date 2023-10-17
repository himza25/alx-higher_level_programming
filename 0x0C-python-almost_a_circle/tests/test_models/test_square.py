#!/usr/bin/python3
"""This module contains all unittests for the Square class."""
import unittest
import os
from models.square import Square
from models.rectangle import Rectangle


class TestSquareClass(unittest.TestCase):
    """This class contains all unittests for the Square class."""

    def test_square_inheritance(self):
        """Test if Square inherits from Rectangle."""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_square_instance(self):
        """Test if square is an instance of Square class."""
        s1 = Square(2)
        self.assertIsInstance(s1, Square)

    def test_size_getter(self):
        """Test size getter."""
        s1 = Square(2)
        self.assertEqual(s1.size, 2)

    def test_size_setter(self):
        """Test size setter."""
        s1 = Square(2)
        s1.size = 3
        self.assertEqual(s1.size, 3)

    def test_str_method(self):
        """Test __str__ method."""
        s1 = Square(2, 2, 2, 99)
        self.assertEqual(str(s1), "[Square] (99) 2/2 - 2")

    def test_update_method_args(self):
        """Test the update method with *args."""
        s1 = Square(2, 2, 2, 99)
        s1.update(100, 5, 7, 8)
        self.assertEqual(str(s1), "[Square] (100) 7/8 - 5")

    def test_update_method_kwargs(self):
        """Test the update method with **kwargs."""
        s1 = Square(2, 2, 2, 99)
        s1.update(id=101, size=6, x=9, y=10)
        self.assertEqual(str(s1), "[Square] (101) 9/10 - 6")

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        s1 = Square(2, 2, 2, 99)
        self.assertEqual(s1.to_dictionary(),
                         {'id': 99, 'size': 2, 'x': 2, 'y': 2})

    def test_invalid_size_type(self):
        """Test with invalid size type."""
        with self.assertRaises(TypeError):
            s1 = Square("2")

    def test_negative_size_value(self):
        """Test with negative size value."""
        with self.assertRaises(ValueError):
            s1 = Square(-2)

    def test_invalid_x_type(self):
        """Test with invalid x type."""
        with self.assertRaises(TypeError):
            s1 = Square(2, "2")

    def test_negative_x_value(self):
        """Test with negative x value."""
        with self.assertRaises(ValueError):
            s1 = Square(2, -2)

    def test_invalid_y_type(self):
        """Test with invalid y type."""
        with self.assertRaises(TypeError):
            s1 = Square(2, 2, "2")

    def test_negative_y_value(self):
        """Test with negative y value."""
        with self.assertRaises(ValueError):
            s1 = Square(2, 2, -2)


if __name__ == "__main__":
    unittest.main()
