#!/usr/bin/python3
"""Unit test for the Base class"""

import unittest
import json
import os
import csv
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def test_id_assignment(self):
        """Test for id assignment"""
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)

    def test_id_assignment_manual(self):
        """Test for manual id assignment"""
        b4 = Base(15)
        self.assertEqual(b4.id, 15)

    def test_to_json_string(self):
        """Test for correct JSON string output"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 1}]), '[{"id": 1}]')

    def test_from_json_string(self):
        """Test for correct JSON string to dictionary conversion"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{"id": 1}])

    def test_save_to_file(self):
        """Test for saving to file"""
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        with open("Base.json", "r") as f:
            self.assertEqual(
                json.loads(f.read()), [{"id": 1}, {"id": 2}])

    def test_load_from_file(self):
        """Test for loading from file"""
        self.assertEqual(Base.load_from_file(), [])

    def test_save_to_file_csv(self):
        """Test for saving to CSV file"""
        print("Debug: Inside test_save_to_file_csv")
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file_csv([b1, b2])

        print("Debug: File should be saved by now. Checking contents...")

        with open("Base.csv", "r", newline='') as f:
            reader = csv.reader(f)
            read_list = list(reader)
            print("Debug: Contents from file:", read_list)
            self.assertEqual(read_list, [["1"], ["2"]])

    def test_load_from_file_csv(self):
        """Test for loading from CSV file"""
        if os.path.exists('Base.csv'):
            os.remove('Base.csv')
        self.assertEqual(Base.load_from_file_csv(), [])


if __name__ == '__main__':
    unittest.main()
