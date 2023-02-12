#!/usr/bin/python3
"""
Unittest module for testing file_storage
module.
"""

import unittest
from uuid import uuid4
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """
    Defines tests for file_storage module.
    """

    def test_is_FileStorage(self):
        """
        Tests to check if a FileModel instance
        is created.
        """
        self.assertTrue(isinstance(storage, FileStorage))

    def test_all(self):
        """
        Tests the return type of storage.all()
        method.
        """
        # new = FileStorage()
        # d = new.all()
        self.assertEqual(type(storage.all()), dict)

    def test_new(self):
        """
        Tests the `new(self, obj)` method
        of FileStorage
        """
        model1 = BaseModel()
        objects = str(storage.all())
        model2 = BaseModel()
        self.assertNotEqual(objects, str(storage.all()))

    def test_save_reload(self):
        """
        Test `save(self)` and `reload(self)`
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
