#!/usr/bin/python3
"""Module for conducting unit tests on the Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io


class RectangleTestCases(unittest.TestCase):
    """Class for testing the Rectangle class."""

    def setUp(self):
        """Initialize attributes for each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Cleanup after each test."""
        pass

    def test_class_type(self):
        """Check the type of the Rectangle class."""
        self.assertEqual(
            str(Rectangle), "<class 'models.rectangle.Rectangle'>")

    def test_is_subclass(self):
        """Check if Rectangle is a subclass of Base."""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_constructor_no_args(self):
        """Test constructor with no arguments."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        self.assertEqual(
            str(e.exception),
            "__init__() missing 2 required positional arguments: "
            "'width' and 'height'")

    def test_constructor_too_many_args(self):
        """Test constructor with too many arguments."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5, 6)
        self.assertEqual(
            str(e.exception),
            "__init__() takes from 3 to 6 positional arguments "
            "but 7 were given")

    def test_constructor_one_arg(self):
        """Test constructor with one argument."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        self.assertEqual(
            str(e.exception),
            "__init__() missing 1 required positional argument: 'height'")

    def test_property_modifications(self):
        """Test property modifications."""
        r = Rectangle(5, 9)
        r.width = 100
        r.height = 101
        r.x = 102
        r.y = 103
        d = {'_Rectangle__height': 101, '_Rectangle__width': 100,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.width, 100)
        self.assertEqual(r.height, 101)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)

    def test_value_validations_negative(self):
        """Test value validations for negative numbers."""
        r = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            s = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_value_validations_zero(self):
        """Test value validations for zero."""
        r = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            s = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, 0)
            self.assertEqual(str(e.exception), s)

    def test_area_method(self):
        """Test area method."""
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)

    def test_display_output(self):
        """Test display method output."""
        r = Rectangle(1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)

    def test_str_representation(self):
        """Test __str__ method."""
        r = Rectangle(5, 2)
        s = '[Rectangle] (1) 0/0 - 5/2'
        self.assertEqual(str(r), s)

    def test_update_attributes(self):
        """Test update method."""
        r = Rectangle(5, 2)
        r.update(10)
        self.assertEqual(r.id, 10)

    def test_to_dict(self):
        """Test to_dictionary method."""
        r = Rectangle(1, 2)
        d = {'x': 0, 'y': 0, 'width': 1, 'id': 1, 'height': 2}
        self.assertEqual(r.to_dictionary(), d)

    def test_instance_creation(self):
        """Test instance creation."""
        r = Rectangle(10, 20)
        self.assertEqual(str(type(r)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 20, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, d)

    def test_property_validations(self):
        """Test property validations."""
    r = Rectangle(1, 2)
    attributes = ["x", "y", "width", "height"]
    for attribute in attributes:
        s = "{} must be an integer".format(attribute)
        invalid_types = [
            3.14, -1.1, float('inf'), float('-inf'), True, "str",
            (2,), [4], {5}, {6: 7}, None
        ]
        for invalid_type in invalid_types:
            with self.assertRaises(TypeError) as e:
                setattr(r, attribute, invalid_type)
            self.assertEqual(str(e.exception), s)

    def test_area_calculation(self):
        """Test area calculation."""
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)

    def test_display_method(self):
        """Test display method."""
        r = Rectangle(1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)

    def test_str_method(self):
        """Test __str__ method."""
        r = Rectangle(5, 2)
        s = '[Rectangle] (1) 0/0 - 5/2'
        self.assertEqual(str(r), s)

    def test_update_method(self):
        """Test update method."""
        r = Rectangle(5, 2)
        r.update(10)
        self.assertEqual(r.id, 10)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        r = Rectangle(1, 2)
        d = {'x': 0, 'y': 0, 'width': 1, 'id': 1, 'height': 2}
        self.assertEqual(r.to_dictionary(), d)


if __name__ == "__main__":
    unittest.main()
