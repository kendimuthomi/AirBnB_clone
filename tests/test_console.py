#!/usr/bin/python3
""" Unittests for the console.py"""

import unittest
import sys
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage

class HBNBCommandTestCases(unittest.TestCase):
    """
    unittests for the class testing prompting 
    of the HBNB Console
    """
    def test_prompt(self):
        """
        Checking if the prompt is correct
        """
        prompt = "(hbnb) "
        self.assertEqual(prompt, HBNBCommand.prompt)

    def test_help(self):
        """
        Testing the various outputs on help *func
        """
        help_quit = "Exits the programme"
        help_create = """
        Creates a new instance of BaseModel,
        saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel
        """
        help_show = """
        Prints the string representation of an instance based
        on the class name and id. Ex: $ show BaseModel 1234-1234-1234
        """
        help_destroy = """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        help_all = """
        Prints all string representation of all instances
        based on the class name or if no class name is provided
        Prints all instances. See usage below
        Ex: $ all BaseModel or $ all
        """
        help_update = """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(help_quit, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(help_create, f.getvalue()[:-1])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(help_show, f.getvalue()[:-1])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(help_destroy, f.getvalue()[:-1])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(help_all, f.getvalue()[:-1])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(help_update, f.getvalue()[:-1])

    def test_create(self):
        """Testing if do_create creates a model and then displays its id"""
        class_missing = "** class name missing **"
        class_error = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            identity = f.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as f:
            all_obs = storage.all()
            print(all_obs[f"User.{identity}"])
            ob_string = f.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f'User.show("{identity}")')
            self.assertEqual(f.getvalue()[:-1], ob_string)
        
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Vashow")
            self.assertEqual(f.getvalue()[:-1], class_error)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue()[:-1], class_missing)

    def test_show(self):
        """
        Testing do_show for all cases seeing whether correct errors displayed
        or if correctly displayed
        format: $ show BaseModel 1234-1234-1234
        """
        class_missing = "** class name missing **"
        id_missing = "** instance id missing **"
        instance_error = "** no instance found **"
        class_error = "** class doesn't exist **"

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            identity = f.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as f:
            all_obs = storage.all()
            print(all_obs[f"User.{identity}"])
            ob_string = f.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {identity}")
            self.assertEqual(f.getvalue()[:-1], ob_string)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue()[:-1], class_missing)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual(f.getvalue()[:-1], id_missing)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show User 123-123-123-123")
            self.assertEqual(f.getvalue()[:-1], instance_error)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show Vashow 123-123-123-123")
            self.assertEqual(f.getvalue()[:-1], class_error)

