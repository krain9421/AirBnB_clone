#!/usr/bin/python3
"""Unittest module for testing `models/user.py`
    module
"""

import unittest
from models.user import User
from datetime import datetime

class Test_User(unittest.TestCase):
    """Defines unittests for user module"""

    def test_instance_uuid_is_unique(self):
        """Tests to check if uuids of different
            instances are unique.
        """
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_instance_created_at_is_str(self):
        """Test to check the type of `created_at`
            attribute
        """
        user1 = User()
        self.assertEqual(type(user1.created_at), datetime)
        self.assertEqual(type(user1.updated_at), datetime)

    def test_save_method(self):
        """Tests to check the `save(self)` method"""
        from time import sleep
        user1 = User()
        sleep(1)
        user1.save()
        self.assertNotEqual(user1.created_at, user1.updated_at)
