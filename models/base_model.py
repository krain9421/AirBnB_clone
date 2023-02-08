#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class

    Fields:
        id (string): The unique id of the object
        created_at (datetime): The time when an instance is created
        updated_at (datetime): The time to be updated when an object
                                is changed
    """
    id = str(uuid.uuid4())
    created_at = datetime.today()
    updated_at = created_at

    def save(self):
        """Updates the public instance attribute `updated_at` with
            the current datetime
        """
        self.updated_at = datetime.now()

    def __str__(self):
        """Return the printable representation of the BaseModel."""
