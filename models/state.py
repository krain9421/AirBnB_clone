#!/usr/bin/python3
"""
state module that defines a State classs.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Defines the class State with the following list of
    class attributes:
    + `name`: string - empty string.
    """
    name = str()
