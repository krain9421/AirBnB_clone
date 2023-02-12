#!/usr/bin/python3
"""Unittest module for testing `models/user.py`
    module
"""

import unittest
from models.user import User
from datetime import datetime


class Test_User(unittest.TestCase):
    """Defines unittests for user module."""

    def test_instance_uuid_is_unique(self):
        """Tests to check if uuids of different
            instances are unique.
        """
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_instance_created_at_is_str(self):
        """Test to check the type of `created_at`
            attribute.
        """
        user1 = User()
        self.assertEqual(type(user1.created_at), datetime)
        self.assertEqual(type(user1.updated_at), datetime)

    def test_save_method(self):
        """Tests to check the `save(self)` method."""
        from time import sleep
        user1 = User()
        sleep(1)
        user1.save()
        self.assertNotEqual(user1.created_at, user1.updated_at)

    def test_representation(self):
        """Tests to check the string
            representation of a User instance.
        """
        user1 = User()
        name = user1.__class__.__name__
        rep = "[{}] ({}) {}".format(name, user1.id, user1.__dict__)
        self.assertEqual(user1.__str__(), rep)

    def test_instance_dictionary(self):
        """Tests to check if a User instance
            can be created from a dictionary.
        """
        user1 = User()
        user1.email = "go@lang.com"
        user1.first_name = "Amy"
        user1.last_name = "Alexandria"
        user1.password = "r00t"
        self.assertTrue("__class__" in user1.to_dict())
        self.assertTrue("email" in user1.to_dict())
        self.assertTrue("first_name" in user1.to_dict())
        self.assertTrue("last_name" in user1.to_dict())
        self.assertTrue("password" in user1.to_dict())

    def test_new_instance_from_dictionary(self):
        """Tests to check if a User instance
            can be created from a dictionary.
        """
        user1 = User()
        model_json = user1.to_dict()
        user2 = User(**model_json)
        self.assertFalse(user1 is user2)

    def test_new_instance_properties_against_old(self):
        """Tests a new instance against an old
            instance.
        """
        user1 = User()
        user1.name = "User1"
        model_json = user1.to_dict()
        user2 = User(**model_json)
        self.assertEqual(type(user1), type(user2))
        self.assertEqual(user1.id, user2.id)
        self.assertEqual(user1.email, user2.email)
        self.assertEqual(user1.first_name, user2.first_name)
        self.assertEqual(user1.last_name, user2.last_name)
        self.assertEqual(user1.password, user2.password)
        self.assertEqual(user1.name, user2.name)


# if __name__ == '__main__':
# unittest.main()
