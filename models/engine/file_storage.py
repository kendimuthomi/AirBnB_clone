#!/usr/bin/python3
import json
from models.base_model import BaseModel

from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        obj_cl_name = obj.__class__.__name__
        FileStorage.__objects[f"{obj_cl_name}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as file:
            my_dict = {}
            for key, my_object in FileStorage.__objects.items():
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
            with open(self.__file_path, 'r',  encoding="utf-8") as file:
                objects_dict = json.load(file)
            for value in objects_dict.values():
                class_name = value["__class__"]
                self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass
