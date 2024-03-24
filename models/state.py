#!/usr/bin/pyhton3
"""Defines the class state."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state.

    Attributes:
        name(str): name of the state.
    """

    name = ""
