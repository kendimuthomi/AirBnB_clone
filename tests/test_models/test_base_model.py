#!/usr/bin/python3
""" This provides automated tests for the class BaseModel """
from models.base_model import BaseModel
import unittest
import uuid
import datetime


class BaseModelTestCase(unittest.TestCase):
    """The unittests of the basemodel"""

    def testInitialisation(self):
        """"Testing if initialising works as intended"""

        my_model = BaseModel()
        new_model = BaseModel()
        self.assertNotEqual(my_model.id, new_model.id)
        self.assertNotEqual(my_model.created_at, new_model.created_at)
        self.assertNotEqual(my_model.updated_at, new_model.updated_at)
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.created_at, datetime.datetime)
        self.assertIsInstance(my_model.updated_at, datetime.datetime)
        self.assertIsInstance(my_model.id, str)


    def testSave(self):
        """Tests the save instance method"""

        my_model = BaseModel()
        initial_datetime = my_model.updated_at
        my_model.save()
        self.assertIsInstance(my_model.updated_at, datetime.datetime)
        self.assertIsNot(my_model.updated_at, initial_datetime)

    def testToDict(self):
        """Tests the to_dict() method"""

        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        for key in my_model_json.keys():
            if (key != '__class__'):
                self.assertIn(key, my_model.__dict__.keys())

        for key, value in my_model_json.items():
            if (key != 'created_at' and key != 'updated_at'\
                    and key != '__class__'):
                self.assertIn(value, my_model.__dict__.values())

        self.assertIn('__class__', my_model_json.keys())
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)


    def testKwargs(self):
        """Tests if basemodel can be initialised for a parsed dict"""

        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        new_model = BaseModel(**my_model_json)
        self.assertEqual(my_model.id, new_model.id)
        self.assertEqual(my_model.created_at, new_model.created_at)
        self.assertEqual(my_model.updated_at, new_model.updated_at)
