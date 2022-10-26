#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        obj_cl_name = obj.__class__.__name__
        my_dict = obj.to_dict()
        my_dict["id"] = str(my_dict["id"])
        self.__objects[f"{obj_cl_name}.{obj.id}"] = my_dict

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "a") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing)

        """
        try:
            with open(self.__file_path, encoding="utf-8") as file:
                self.__objects = json.load(file)

        except FileNotFoundError:
            pass

