#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        obj_cl_name = obj.__class__.__name__
        FileStorage.__objects[f"{obj_cl_name}.{obj.id}"] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        
