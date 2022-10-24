#!/usr/bin/python3
""" This provides automated tests for the class BaseModel """
from models.base_model import BaseModel
import unittest

class BaseModelTestCase(unittest.TestCase):
    """The unittests of the basemodel"""

    def testInitialisation(self):
        """"Testing if initialising works as intended"""

        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertIsInstance(my_model.id, uuid)


    def testSave(self):
        """Tests the save instance method"""

        my_model = BaseModel()
        initial_datetime = my_model.updated_at
        my_model.save()
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertIsNot(my_model.updated_at, initial_datetime)

    def testToDict(self):
        """Tests the to_dict() method"""

        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        self.assertIn(my_model_json.keys(), my_model.to_dict().keys())
        self.assertIn(my_model_json.values(), my_mode.to_dict().values())
        self.assertIn('__class__', my_model_json.keys())
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)

