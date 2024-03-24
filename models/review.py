#!/usr/bin/python3
"""Defines a class review."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review.

    Attributes:
        place_id(str): The id of a place.
        user_id(str): The id of the user.
        text(str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
