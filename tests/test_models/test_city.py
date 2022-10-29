#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City


class CityTestCase(unittest.TestCase):
    """unittests for the subclass City"""

    def setUp(self):
        self.c = City()

    def test_class_attributes(self):
        self.assertIs(type(self.c.state_id), str)
        self.assertIs(type(self.c.name), str)

    def test_attr_are_class_attr(self):
        self.assertTrue(hasattr(self.c, "state_id"))
        self.assertTrue(hasattr(self.c, "name"))

    def test_city_is_basemodel_subclass(self):
        self.assertTrue(issubclass(type(self.c), BaseModel))
