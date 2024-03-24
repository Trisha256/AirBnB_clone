#!/usr/bin/python3
"""Defines the class place."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents the place.

    Attributes:
        city_id(str): Its the City.id.
        user_id(str): The User.id.
        name(str): Name of the place.
        description(str): Description of the place.
        number_rooms(int): Number of rooms.
        number_bathrooms(int): Number of bathrooms.
        max_guest(int): The maximum number of guests.
        price_by_night(int): The price per night.
        latitude(float): The latitude of the place.
        longitude(float): The longitude of the place.
        amenity_ids(list): A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
