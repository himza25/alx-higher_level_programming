#!/usr/bin/python3
"""This module defines test cases for the Base class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def test_init(self):
        """Test initialization of the Base class"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_to_json_string(self):
        """Test the to_json_string method"""
        list_dicts = [{"id": 1}, {"id": 2}]
        expected = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(Base.to_json_string(list_dicts), expected)

    def test_from_json_string(self):
        """Test the from_json_string method"""
        json_str = '[{"id": 1}, {"id": 2}]'
        expected = [{"id": 1}, {"id": 2}]
        self.assertEqual(Base.from_json_string(json_str), expected)


if __name__ == '__main__':
    unittest.main()
