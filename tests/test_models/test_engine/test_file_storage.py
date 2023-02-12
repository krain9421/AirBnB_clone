#!/usr/bin/python3
"""Unittests for file_storage module"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


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

    def test_new(self):
        """Tests the `new(self, obj)` method
            of FileStorage
        """
        new = BaseModel()
        objects = str(storage.all())
        new = BaseModel()
        objects2 = str(storage.all())
        self.assertNotEqual(objects, objects2)

    def test_save_reload(self):
        """Test `save(self)` and `reload(self)`
            methods of the FileStorage class.
        """
        storage.reload()
        objects1 = str(storage.all())
        new = BaseModel()
        storage.save()
        storage.reload()
        objects2 = str(storage.all())
        self.assertNotEqual(objects1, objects2)

    if __name__ == '__main__':
        unittest.main()
