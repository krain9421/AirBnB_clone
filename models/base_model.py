#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class

    Attributes:
        id (string): The unique id of the object
        created_at (datetime): The time when an instance is created
        updated_at (datetime): The time to be updated when an object
                                is changed
    """

    def __init__(self):
        """Initializes the BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at

    def save(self):
        """Updates the public instance attribute `updated_at` with
            the current datetime
        """
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns the printable representation of the BaseModel."""
        repr = "[BaseModel] " + "(" + self.id + ") "
        repr += str(self.__dict__)
        return (repr)

    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__
            of the instance
        """
        dict = self.__dict__.copy()
        dict.update(__class__="BaseModel")
        dict.update(created_at=self.created_at.isoformat())
        dict.update(updated_at=self.updated_at.isoformat())
        return (dict)
