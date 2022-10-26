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
        self.__objects[f"{obj_cl_name}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as file:
            my_dict = {}
            for key, my_object in self.__objects.items():
                obj_class_name = my_object.__class__.__name__
                my_dict[key] = my_object.to_dict()
            json.dump(my_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing)

        """
        try:
            with open(self.__file_path, encoding="utf-8") as file:
                objects_dict = json.load(file)
            for key, value in objects_dict.items():
                model = BaseModel(**value)
                obj_cl_name = model.__class__.__name__
                self.__objects[key] = model

        except FileNotFoundError:
            pass
