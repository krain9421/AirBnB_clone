#!/usr/bin/python3
"""User module that inherits from a BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines a User class that inherits from
    BaseModel with the following attributes.
    + email(string): empty string
    + password(string): empty string
    + first_name(string): empty string
    + last_name(string): empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
