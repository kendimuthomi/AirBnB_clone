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
        self.assertIs(type(self.state.name), str)

    def test_attr_are_class_attr(self):
        self.assertTrue(hasattr(self.state, "name"))

    def test_state_is_an_instance_of_basemodel(self):
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_instances_stored_in_obj(self):
        self.assertIn(self.state, storage.all().values())

    def test_two_states_have_diff_ids(self):
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)
