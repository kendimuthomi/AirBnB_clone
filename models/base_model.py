#!/usr/bin/python3
"""Defining the BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Represents the BaseModel for the hbnb project"""
    def __init__(self, *args, **kwargs):
        """
        initializes a new BaseModel
        using **kwargs(key word arguments)

        """
        format_str = '%Y-%m-%dT%H:%M:%S.%f'
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, format_str)
                else:
                    if key != "__class__":
                        self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """returns the representation of the BaseModel instance"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at with the current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all key/value of __dict__"""
        format_str = '%Y-%m-%dT%H:%M:%S.%f'
        model_dict = self.__dict__.copy()
        model_dict["created_at"] = self.created_at.strftime(format_str)
        model_dict["updated_at"] = self.updated_at.strftime(format_str)
        model_dict["__class__"] = self.__class__.__name__
        return model_dict
