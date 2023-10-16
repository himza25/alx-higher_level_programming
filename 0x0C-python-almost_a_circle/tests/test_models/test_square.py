#!/usr/bin/python3
"""Module for Rectangle unit tests."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class."""

    def setUp(self):
        """Resets the object count to 0."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Cleanup after each test."""
        pass

    def test_class_type(self):
        """Tests Rectangle class type."""
        self.assertEqual(
            str(Rectangle), "<class 'models.rectangle.Rectangle'>")

    def test_inheritance(self):
        """Tests if Rectangle inherits Base."""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_constructor_no_args(self):
        """Tests constructor with no arguments."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        self.assertEqual(
            str(e.exception),
            "__init__() missing 2 required positional arguments: "
            "'width' and 'height'")

    def test_constructor_many_args(self):
        """Tests constructor with too many arguments."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5, 6)
        self.assertEqual(
            str(e.exception),
            "__init__() takes from 3 to 6 positional arguments "
            "but 7 were given")

    def test_instantiation(self):
        """Tests instantiation."""
        r = Rectangle(10, 20)
        self.assertEqual(
            str(type(r)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(r, Base))

    def test_properties(self):
        """Tests property getters and setters."""
        r = Rectangle(5, 9)
        r.width = 98
        r.height = 99
        r.x = 102
        r.y = 103
        self.assertEqual(r.width, 98)
        self.assertEqual(r.height, 99)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)

    def invalid_types(self):
        """Returns tuple of invalid types for validation."""
        return (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
                [4], {5}, {6: 7}, None)

    def test_property_validation(self):
        """Tests property validation."""
        r = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            msg = "{} must be an integer".format(attribute)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attribute, invalid_type)
                self.assertEqual(str(e.exception), msg)

    def test_property_value_validation(self):
        """Tests property value validation."""
        r = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            msg = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, 0)
            self.assertEqual(str(e.exception), msg)

    def test_area(self):
        """Tests area computation."""
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_str_method(self):
        """Tests __str__ method."""
        r = Rectangle(5, 10, 15, 20, 25)
        self.assertEqual(str(r), "[Rectangle] (25) 15/20 - 5/10")

    def test_to_dictionary(self):
        """Tests to_dictionary method."""
        r = Rectangle(10, 20, 30, 40, 50)
        expected_dict = {'id': 50, 'width': 10, 'height': 20, 'x': 30, 'y': 40}
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
