#!/usr/bin/python3
"""
city module containing City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines the class City with the following list of
    class attributes:
    + `state_id`: string - empty string: it will be the State.id
    + `name`: string - empty string
    """
    state_id = str()
    name = str()
