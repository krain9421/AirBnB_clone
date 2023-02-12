#!/usr/bin/env python3
"""
Unittest module for testing `city` module
"""


import unittest
from models.city import City
from datetime import datetime


class Test_City(unittest.TestCase):
    """
    Test the basic features of the City class.
    """

    def test_instance_uuid_is_unique(self):
        """
        Tests if uuid is unique for each
        instance.
        """
        user1 = City()
        user2 = City()
        self.assertNotEqual(user1.id, user2.id)

    def test_instance_created_at_is_str(self):
        """
        Tests for the datetime attributes of City
        object.
        """
        user1 = City()
        self.assertEqual(type(user1.created_at), datetime)
        self.assertEqual(type(user1.updated_at), datetime)

    def test_save_method(self):
        """
        Tests the `save(self)` method of City.
        """
        user1 = City()
        user1.save()
        self.assertNotEqual(user1.created_at, user1.updated_at)

    def test_representation(self):
        """
        Tests to check the string representation
        of City instance.
        """
        user1 = City()
        name = user1.__class__.__name__
        string = "[{}] ({}) {}".format(name, user1.id, user1.__dict__)
        self.assertEqual(user1.__str__(), string)

    def test_instance_dictionary(self):
        """
        Tests to check the dictionary representation
        of City instance.
        """
        user1 = City()
        user1.name = "New Instance variable"
        self.assertTrue("__class__" in user1.to_dict())
        self.assertTrue("name" in user1.to_dict())

    def test_new_instance_from_dictionary(self):
        """
        Tests to check if a City class can be created
        from a dictionary.
        """
        user1 = City()
        model_json = user1.to_dict()
        user2 = City(**model_json)
        self.assertFalse(user1 is user2)


# if __name__ == '__main__':
# unittest.main()
