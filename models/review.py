#!/usr/bin/python3
from models.base_model import BaseModel
"""Defines a class review"""


class Review(BaseModel):
    """
    Representation of the
    class Review

    Attribute:
    text: review text
    place_id: Place.id
    user_id: User.id
    """

    text = ""
    place_id = ""
    user_id = ""
