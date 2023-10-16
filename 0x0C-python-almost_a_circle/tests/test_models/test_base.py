#!/usr/bin/python3
"""This module contains unit tests for the Base class."""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTestCase(unittest.TestCase):
    """Class for testing the Base class."""

    def setUp(self):
        """Reset the Base class attribute before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Cleanup after each test."""
        pass

    def test_private_attribute_nb_objects(self):
        """Verify if nb_objects is private."""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_initial_value_of_nb_objects(self):
        """Check if nb_objects initializes to zero."""
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_instance_creation(self):
        """Test Base class instantiation."""
        instance = Base()
        self.assertIsInstance(instance, Base)
        self.assertEqual(instance.__dict__, {"id": 1})
        self.assertEqual(instance.id, 1)

    def test_constructor_signature(self):
        """Test constructor's argument requirements."""
        with self.assertRaises(TypeError) as context:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(context.exception), msg)

    def test_constructor_with_extra_args(self):
        """Test constructor with more than one argument."""
        with self.assertRaises(TypeError) as context:
            Base.__init__(self, 1, 2)
        msg = ("__init__() takes from 1 to 2 positional arguments "
               "but 3 were given")
        self.assertEqual(str(context.exception), msg)

    def test_sequential_ids(self):
        """Test if IDs are sequential."""
        instance1 = Base()
        instance2 = Base()
        self.assertEqual(instance1.id + 1, instance2.id)

    def test_id_sync(self):
        """Test if class attribute and instance ID are in sync."""
        instance = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), instance.id)

    def test_id_sync_more(self):
        """Test if class attribute and instance ID are in sync."""
        instance = Base()
        instance = Base("Foo")
        instance = Base(98)
        instance = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), instance.id)

    def test_custom_id_as_int(self):
        """Test custom integer ID."""
        custom_id = 98
        instance = Base(custom_id)
        self.assertEqual(instance.id, custom_id)

    def test_custom_id_as_str(self):
        """Test custom string ID."""
        custom_id = "FooBar"
        instance = Base(custom_id)
        self.assertEqual(instance.id, custom_id)

    def test_id_as_keyword_arg(self):
        """Test ID passed as a keyword argument."""
        custom_id = 421
        instance = Base(id=custom_id)
        self.assertEqual(instance.id, custom_id)

    # Tests for to_json_string method
    def test_to_json_string(self):
        """Test the to_json_string method."""
        with self.assertRaises(TypeError) as context:
            Base.to_json_string()
        msg = ("to_json_string() missing 1 required positional "
               "argument: 'list_dictionaries'")
        self.assertEqual(str(context.exception), msg)

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

        dict_list = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(len(Base.to_json_string(dict_list)),
                         len(str(dict_list)))

    # Tests for from_json_string method
    def test_from_json_string(self):
        """Test the from_json_string method."""
        with self.assertRaises(TypeError) as context:
            Base.from_json_string()
        msg = ("from_json_string() missing 1 required positional "
               "argument: 'json_string'")
        self.assertEqual(str(context.exception), msg)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        json_str = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        dict_list = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(Base.from_json_string(json_str), dict_list)

    # Tests for save_to_file method
    def test_save_to_file(self):
        """Test the save_to_file method."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

    # Tests for create method
    def test_create(self):
        """Test the create method."""
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    # Tests for load_from_file method
    def test_load_from_file(self):
        """Test the load_from_file method."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_in = [r1, r2]
        Rectangle.save_to_file(list_in)
        list_out = Rectangle.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))


if __name__ == "__main__":
    unittest.main()
