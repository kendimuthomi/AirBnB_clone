#!/usr/bin/python3
""" Contains unittests for file_storage.py"""
import unittest
from models import storage
from models.base_model import BaseModel
import datetime
import json
from models.engine.file_storage import FileStorage


class FileStorageTestCase(unittest.TestCase):
    """Defiinition of the class for the unittests"""

    def test_file_path_is_a_private_class_attr(self):
        """Checks that file_path is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__file_path"))

    def test_All(self):
        """
        Testing the method all() from FileStorage
        Initially when there is no file.json

        """
        all_objs = storage.all()
        new_model_1 = BaseModel()
        new_model_2 = BaseModel()
        new_model_3 = BaseModel()

        all_objs = storage.all()
        objs = []
        for obj in all_objs.values():
            objs.append(obj)

        self.assertIn(new_model_1, objs)
        self.assertIn(new_model_2, objs)
        self.assertIn(new_model_3, objs)

    def test_New(self):
        """Testing the method new()"""
        new_model = BaseModel()
        all_objs = storage.all()
        obj_values = []
        for obj in all_objs.values():
            for value in obj.to_dict().values():
                obj_values.append(value)

        self.assertIsInstance(new_model, BaseModel)
        self.assertIn(new_model.id, obj_values)
        self.assertIn(new_model.created_at.isoformat(), obj_values)
        self.assertIn(new_model.updated_at.isoformat(), obj_values)

    def test_Save(self):
        """Testing the methon save()"""
        model = BaseModel()
        model_1 = BaseModel()
        model_2 = BaseModel()
        storage.save()
        with open("file.json", encoding="utf-8") as f:
            all_dicts = json.load(f)

        objects_ids = []
        for obj in all_dicts.values():
            objects_ids.append(obj["id"])

        self.assertIn(model.id, objects_ids)
        self.assertIn(model_1.id, objects_ids)
        self.assertIn(model_2.id, objects_ids)

