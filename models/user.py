#!/usr/bin/python3
from models.base_model import BaseModel
"""
Defines the class User
that iherits from BaseModel
"""

class User(BaseModel):
    """
    Representation of a user.

    Attributes:
    email(str): the users's email
    password(str): user's password
    first_name(str): user's first name
    last_name(str): user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
