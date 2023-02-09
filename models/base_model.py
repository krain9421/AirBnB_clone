#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class

    Attributes:
        id (string): The unique id of the object
        created_at (datetime): The time when an instance is created
        updated_at (datetime): The time to be updated when an object
                                is changed
    """

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel"""
        if kwargs:
            self.id = kwargs.get('id')
            self.created_at = datetime.fromisoformat(kwargs.get('created_at'))
            self.update_at = datetime.fromisoformat(kwargs.get('updated_at'))
            kwargs.pop('id')
            kwargs.pop('created_at')
            kwargs.pop('updated_at')
            self.__dict__.update(kwargs)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Updates the public instance attribute `updated_at` with
            the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """Returns the printable representation of the BaseModel."""
        rep = "[BaseModel] " + "(" + self.id + ") "
        rep += str(self.__dict__)
        return (rep)

    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__
            of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict.update(__class__="BaseModel")
        my_dict.update(created_at=self.created_at.isoformat())
        my_dict.update(updated_at=self.updated_at.isoformat())
        return (my_dict)
