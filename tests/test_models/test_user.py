#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage


class UserTestCase(unittest.TestCase):
    """The unittest for the User class"""

    def setUp(self):
        self.u = User()

    def test_class_attrs(self):
        """Test the class attributes"""
        self.assertIs(type(self.u.email), str)
        self.assertIs(type(self.u.last_name), str)
        self.assertIs(type(self.u.first_name), str)
        self.assertIs(type(self.u.password), str)

    def test_attrs_are_class_attrs(self):
        """Test if the attributes are class attributes"""
        self.assertTrue(hasattr(self.u, "first_name"))
        self.assertTrue(hasattr(self.u, "last_name"))
        self.assertTrue(hasattr(self.u, "password"))
        self.assertTrue(hasattr(self.u, "email"))

    def test_user_is_an_instance_of_basemodel(self):
        """test if the class User is an instance of BaseModel class"""
        self.assertTrue(issubclass(type(self.u), BaseModel))

    def test_instances_stored_in_objescts(self):
        """tests if the instances of amenity are stored in __objects"""
        self.assertIn(self.u, storage.all().values())

    def test_two_users_have_unique_ids(self):
        """tests if two instances of the subclass User have unique ids"""
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)
