#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City
from models import storage


class CityTestCase(unittest.TestCase):
    """unittests for the subclass City"""

    def setUp(self):
        self.c = City()

    def test_class_attributes(self):
        """tests that all attr passed are the correct types"""
        self.assertIs(type(self.c.state_id), str)
        self.assertIs(type(self.c.name), str)

    def test_attr_are_class_attr(self):
        """tests that all city attr are passed"""
        self.assertTrue(hasattr(self.c, "state_id"))
        self.assertTrue(hasattr(self.c, "name"))

    def test_city_is_basemodel_subclass(self):
        """tests that City is an instance of BaseModel"""
        self.assertTrue(issubclass(type(self.c), BaseModel))

    def test_instances_stored_in_objects(self):
        """checks if the instances of city are stored in __objects"""
        self.assertIn(self.c, storage.all().values())

    def test_two_city_instances_have_different_ids(self):
        """tests that each instance of city has an unique id"""
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)
