#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage


class AmenityTestCase(unittest.TestCase):
    """The unittest for the subclass Amenity"""
    def setUp(self):
        self.a = Amenity()

    def test_class_attributes(self):
<<<<<<< HEAD
=======
        """tests the class attributes"""
>>>>>>> origin/kendi
        self.assertIs(type(self.a.name), str)

    def test_attr_are_cls_atrr(self):
        """tests that these are class attributes"""
        self.assertTrue(hasattr(self.a, "name"))

    def test_if_basemodel_subclass(self):
        """test if amenity is a subclass of basemodel"""
        self.assertTrue(issubclass(type(self.a), BaseModel))

    def test_instances_stored_in_objects(self):
        """tests if the instances of amenity are stored in __objects"""
        self.assertIn(self.a, storage.all().values())

    def test_two_amenities_have_unique_ids(self):
        """tests if two instances of the subclass amenity have unique ids"""
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)

