#!/usr/bin/python3
from models.base_model import BaseModel
"""Defines a class place"""

class Place(BaseModel):
    """
    Representation of the
    class Place

    Attribute:
    name: name of the place
    city_id: City.id
    user_id: User.id
    desciption: a description of the place
    number_rooms: number of rooms
    number_bathrooms: number of bathrooms
    max_guest: maximum number of guests
    price_by_night: price per night
    latitide: the latitude
    longitude: the longitude
    amenity_ids: list of Amenity.ids
    """
    
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
