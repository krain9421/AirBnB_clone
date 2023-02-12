#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods
    for other classes
"""
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
        """Function that initializes the BaseModel"""
        # tformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.fromisoformat(v)
                elif k == "__class__":
                    pass
                else:
                    self.__dict__[k] = v

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.now()
            # print("--------DEBUGGING--------")
            # print("created object:\n{}".format(self.__dict__))
            # print("--------DEBUGGING--------")
            storage.new(self)

    def save(self):
        """Updates the public instance attribute `updated_at` with
            the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """Returns the printable representation of the BaseModel."""
        rep = self.__class__.__name__
        return "[{}] ({}) {}".format(rep, self.id, self.__dict__)

    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__
            of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict.update(__class__=self.__class__.__name__)
        my_dict.update(created_at=self.created_at.isoformat())
        my_dict.update(updated_at=self.updated_at.isoformat())
        return my_dict
