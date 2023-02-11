#!/usr/bin/python3
"""Unittests for base_model module"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Defines unittests for base_model module"""

    def test_is_BaseModel(self):
        """Tests to check if a BaseModel instance
            is created.
        """
        new = BaseModel()
        name = type(new).__name__
        self.assertEqual(name, "BaseModel")

    def test_print_BaseModel(self):
        """Tests to check the result of the string
            representation of a BaseModel instance
        """
        new = BaseModel()
        name = type(new).__name__
        rep = "[{}] ({}) {}".format(name, new.id, new.__dict__)

if __name__ == '__main__':
    unittest.main()
