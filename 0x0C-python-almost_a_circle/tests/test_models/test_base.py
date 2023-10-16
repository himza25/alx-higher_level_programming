#!/usr/bin/python3
"""This module defines tests for class Base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests to check the functionality of Base class"""

    def test_base_id_none(self):
        """Test for Base with id None"""
        base = Base()
        self.assertEqual(base.id, 1)

    def test_base_id_set(self):
        """Test for Base with id set"""
        base = Base(5)
        self.assertEqual(base.id, 5)

    def test_to_json_string_none(self):
        """Test to_json_string with None"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string_none(self):
        """Test from_json_string with None"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string"""
        self.assertEqual(Base.from_json_string(""), [])


if __name__ == "__main__":
    unittest.main()
