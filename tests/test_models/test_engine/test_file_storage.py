#!/usr/bin/python3
"""Unittests for file_storage module"""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Defines unittest for file_storage module"""

    def test_is_FileStorage(self):
        """Tests to check if a FileModel instance
            is created.
        """
        new = FileStorage()
        name = type(new).__name__
        self.assertEqual(name, "FileStorage")

    def test_storage_all(self):
        """Tests the return type of storage.all()
            method.
        """
        new = FileStorage()
        d = new.all()
        self.assertEqual(type(d), dict)

    if __name__ == '__main__':
        unittest.main()
