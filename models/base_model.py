#!/usr/bin/python3
"""Defines the BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """Represents the BaseModel for the hbnb project"""

    def __init__(self):
        """initializes a new BaseModel"""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns the representation of the BaseModel instance"""
        class_name = self.__class__.__name__
        return f"[{(class_name)}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at with the current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all key/value of __dict__"""
        model_dict = self.__dict__.copy()
        model_dict["created_at"] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        model_dict["updated_at"] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        model_dict["__class__"] = self.__class__.__name__
        return model_dict
