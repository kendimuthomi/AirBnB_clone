#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.review import Review
from models import storage


class ReviewTestCase(unittest.TestCase):
    """unittests for the subclass Review"""

    def setUp(self):
        self.r = Review()

    def test_class_attributes(self):
        """tests that all attr are the right type"""
        self.assertIs(type(self.r.place_id), str)
        self.assertIs(type(self.r.user_id), str)
        self.assertIs(type(self.r.text), str)

    def test_attr_are_class_attr(self):
        """tests that all attr are available"""
        self.assertTrue(hasattr(self.r, "place_id"))
        self.assertTrue(hasattr(self.r, "user_id"))
        self.assertTrue(hasattr(self.r, "text"))

    def test_review_is_basemodel_subclass(self):
        """tests that all instances of review are a subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.r), BaseModel))

    def test_if_instances_stored_in_dict(self):
        """tests that review is stored in __objects"""
        self.assertIn(self.r, storage.all().values())

    def test_two_reviews_have_diff_ids(self):
        """tests that all instances of review have a unique id"""
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)
