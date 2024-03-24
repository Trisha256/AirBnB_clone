#!/usr/bin/python3
"""Defines a city."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents the city.

    Attributes:
        state_id(str): state id.
        name(str): name of the city.
    """

    state_id = ""
    name = ""
