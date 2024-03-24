#!/usr/bin/python3
"""Defines the amenity."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents the Amenity.

    Attributes:
        name(str): name of the Amenity.
    """

    name = ""
