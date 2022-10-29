#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.review import Review


class ReviewTestCase(unittest.TestCase):
    """unittests for the subclass Review"""

    def setUp(self):
        self.r = Review()

    def test_class_attributes(self):
        self.assertIs(type(self.r.place_id), str)
        self.assertIs(type(self.r.user_id), str)
        self.assertIs(type(self.r.text), str)

    def test_attr_are_class_attr(self):
        self.assertTrue(hasattr(self.r, "place_id"))
        self.assertTrue(hasattr(self.r, "user_id"))
        self.assertTrue(hasattr(self.r, "text"))

    def test_review_is_basemodel_subclass(self):
        self.assertTrue(issubclass(type(self.r), BaseModel))
