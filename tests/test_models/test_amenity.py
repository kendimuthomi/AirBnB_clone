#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class AmenityTestCase(unittest.TestCase):
    """The unittest for the subclass Amenity"""

    def test_class_attributes(self):
        a = Amenity()
        self.assertIs(type(a.name), str)

    def test_attr_are_cls_atrr(self):
        """tests that these are class attributes"""
        a = Amenity()
        self.assertTrue(hasattr(Amenity, "name"))

    def test_if_basemodel_subclass(self):
        a = Amenity()
        self.assertTrue(issubclass(type(a), BaseModel))
