#!/usr/bin/python3
"""tests for the State subclass"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage


class StateTestCase(unittest.TestCase):
    """The unittests for the State class"""

    def setUp(self):
        self.state = State()

    def test_class_attributes(self):
        """tests the class attributes"""
        self.assertIs(type(self.state.name), str)

    def test_attr_are_class_attr(self):
        """tests that these are class attributes"""
        self.assertTrue(hasattr(self.state, "name"))

    def test_state_is_an_instance_of_basemodel(self):
        """test if state is a subclass of basemodel"""
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_instances_stored_in_obj(self):
        """tests if the instances of state are stored in __objects"""
        self.assertIn(self.state, storage.all().values())

    def test_two_states_have_diff_ids(self):
        """tests if two instances of the subclass state have unique ids"""
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)
