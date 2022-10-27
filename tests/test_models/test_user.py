#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User


class UserTestCase(unittest.TestCase):
    """The unittest for the User class"""

    def test_class_attrs(self):
        """Test the class attributes"""
        u = User()
        self.assertIs(type(u.email), str)
        self.assertIs(type(u.last_name), str)
        self.assertIs(type(u.first_name), str)
        self.assertIs(type(u.password), str)

    def test_attrs_are_class_attrs(self):
        """Test if the attributes are class attributes"""
        u = User()
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "email"))

    def test_user_is_an_instance_of_basemodel(self):
        """test if the class User is an instance of BaseModel class"""
        u = User()
        self.assertTrue(issubclass(type(u), BaseModel))
