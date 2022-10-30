#!/usr/bin/self.python3
import unittest
from models.base_model import BaseModel
from models.place import Place
from models import storage


class PlaceTestCase(unittest.TestCase):
    """unittests for the subclass self.p"""

    def setUp(self):
        self.p = Place()

    def test_class_attributes(self):
        self.assertIs(type(self.p.city_id), str)
        self.assertIs(type(self.p.user_id), str)
        self.assertIs(type(self.p.name), str)
        self.assertIs(type(self.p.description), str)
        self.assertIs(type(self.p.number_rooms), int)
        self.assertIs(type(self.p.number_bathrooms), int)
        self.assertIs(type(self.p.max_guest), int)
        self.assertIs(type(self.p.price_by_night), int)
        self.assertIs(type(self.p.latitude), float)
        self.assertIs(type(self.p.longitude), float)
        self.assertIs(type(self.p.amenity_ids), list)

    def test_attr_are_class_attr(self):
        self.assertTrue(hasattr(self.p, "city_id"))
        self.assertTrue(hasattr(self.p, "user_id"))
        self.assertTrue(hasattr(self.p, "name"))
        self.assertTrue(hasattr(self.p, "description"))
        self.assertTrue(hasattr(self.p, "number_rooms"))
        self.assertTrue(hasattr(self.p, "number_bathrooms"))
        self.assertTrue(hasattr(self.p, "max_guest"))
        self.assertTrue(hasattr(self.p, "price_by_night"))
        self.assertTrue(hasattr(self.p, "latitude"))
        self.assertTrue(hasattr(self.p, "longitude"))
        self.assertTrue(hasattr(self.p, "amenity_ids"))

    def test_place_is_instance_of_basemodel(self):
        self.assertTrue(issubclass(type(self.p), BaseModel))

    def test_instance_stored_in_objects(self):
        self.assertIn(self.p, storage.all().values())

    def test_two_places_have_diff_ids(self):
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)
