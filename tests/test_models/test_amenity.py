#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class AmenityTestCase(unittest.TestCase):
    """The unittest for the subclass Amenity"""
    def setUp(self):
        self.a = Amenity()

    def test_class_attributes(self):
        self.assertIs(type(self.a.name), str)

    def test_attr_are_cls_atrr(self):
        """tests that these are class attributes"""
        self.assertTrue(hasattr(self.a, "name"))

    def test_if_basemodel_subclass(self):
        self.assertTrue(issubclass(type(self.a), BaseModel))
