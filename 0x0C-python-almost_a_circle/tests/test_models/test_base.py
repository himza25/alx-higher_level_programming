#!/usr/bin/python3
"""Unit tests for Base class"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Unit tests for Base class"""

    def test_id(self):
        """Test for id attribute"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)
