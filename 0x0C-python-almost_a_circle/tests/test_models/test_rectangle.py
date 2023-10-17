#!/usr/bin/python3
"""Unit tests for the Rectangle class"""

import unittest
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def test_init(self):
        """Tests for the __init__ method"""
        r = Rectangle(5, 10, 0, 0, 12)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 12)

    def test_area(self):
        """Tests for the area method"""
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        """Tests for the display method"""
        import sys
        from io import StringIO

        r = Rectangle(2, 3)
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##\n##\n##\n")

    def test_str(self):
        """Tests for the __str__ method"""
        r = Rectangle(5, 10, 1, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 1/1 - 5/10")

    def test_update_args(self):
        """Tests for the update method with *args"""
        r = Rectangle(5, 10)
        r.update(12, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (12) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Tests for the update method with **kwargs"""
        r = Rectangle(5, 10)
        r.update(id=12, width=2, height=3, x=4, y=5)
        self.assertEqual(str(r), "[Rectangle] (12) 4/5 - 2/3")

    def test_to_dictionary(self):
        """Tests for the to_dictionary method"""
        r = Rectangle(5, 10, 2, 2, 12)
        self.assertEqual(r.to_dictionary(), {
            'id': 12,
            'width': 5,
            'height': 10,
            'x': 2,
            'y': 2
        })


if __name__ == '__main__':
    unittest.main()
