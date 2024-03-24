#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User.

    Attributes:
        email(str): email of the user.
        password(str): password of the user.
        first_name(str): firstname of the user.
        last_name(str): lastname of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
