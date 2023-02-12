#!/usr/bin/python3
"""Unittests for base_model module"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Defines unittests for base_model module"""

    def test_is_BaseModel(self):
        """Tests to check if a BaseModel instance
            is created.
        """
        new = BaseModel()
        name = type(new).__name__
        self.assertEqual(name, "BaseModel")

    def test_representation(self):
        """Tests to check the result of the string
            representation of a BaseModel instance
        """
        new = BaseModel()
        name = type(new).__name__
        rep = "[{}] ({}) {}".format(name, new.id, new.__dict__)
        self.assertEqual(new.__str__(), rep)

    def test_uuid(self):
        """Tests to check if instances of BaseModel
            have unique `id` attribute value.
        """
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_datetime(self):
        """Tests to check if `updated_at` attribute
            is a datetime object.
        """
        new = BaseModel()
        self.assertEqual(type(new.updated_at), datetime)
        self.assertEqual(type(new.created_at), datetime)

    def test_save(self):
        """Tests to check if `save(self)` method
            updates the `updated_at` attribute
        """
        new = BaseModel()
        updated1 = new.updated_at
        new.save()
        updated2 = new.updated_at
        self.assertNotEqual(updated1, updated2)

    def test_to_dict(self):
        """Tests to check the `to_dict` method
            of BaseModel
        """
        new = BaseModel()
        new.age = 10
        new_dict = new.to_dict()
        self.assertTrue("age" in new_dict)
        self.assertTrue("created_at" in new_dict)
        self.assertTrue("updated_at" in new_dict)
        self.assertTrue("id" in new_dict)
        self.assertTrue("__class__" in new_dict)

    def test_instance_from_dictionary(self):
        """Tests creating a BaseModel instance
            from a dictionary.
        """
        model1 = BaseModel()
        model1_json = model1.to_dict()
        model2 = BaseModel(**model1_json)
        self.assertFalse(model1 is model2)

    def test_instance_datetime_attributes(self):
        """Tests to check the datetime values of
            different instances.
        """
        model1 = BaseModel()
        model1_json = model1.to_dict()
        model2 = BaseModel(**model1_json)
        self.assertEqual(type(model2.created_at), datetime)
        self.assertEqual(type(model2.updated_at), datetime)


# if __name__ == '__main__':
# unittest.main()
