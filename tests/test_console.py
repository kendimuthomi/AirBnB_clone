#!/usr/bin/python3
"""
Unittests for the console.py
in hopes of catching out the edge cases
"""
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
    maxDiff = None

    def test_prompt(self):
        """
        Checking if the prompt in the console is correct
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
            self.assertEqual(f.getvalue().strip(), ob_string)

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

    def test_destroy(self):
        """
        Testing do_destroy for all cases and seeing
        whether correct errors displayed if prompt is flawed
        or if correctly displayed
        format: $ destroy BaseModel 1234-1234-1234
        """
        class_missing = "** class name missing **"
        id_missing = "** instance id missing **"
        instance_error = "** no instance found **"
        class_error = "** class doesn't exist **"

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            identity = f.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as f:
            all_obs = storage.all()
            print(all_obs[f"State.{identity}"])
            ob_string = f.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"show State {identity}")
            self.assertEqual(f.getvalue()[:-1], ob_string)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue()[:-1], class_missing)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy State")
            self.assertEqual(f.getvalue()[:-1], id_missing)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy State 123-123-123-123")
            self.assertEqual(f.getvalue()[:-1], instance_error)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Vashow 123-123-123-123")
            self.assertEqual(f.getvalue()[:-1], class_error)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy State {identity}")
            HBNBCommand().onecmd(f"show State {identity}")
            self.assertEqual(f.getvalue()[:-1], instance_error)

    def test_all(self):
        """
        Testing do_all for all cases and seeing
        whether correct errors displayed if prompt is flawed
        or if correctly displayed
        format: $ $ all BaseModel or $ all
        """
        storage.reload()
        all_obs = storage.all()
        obs_list = []
        error = "** class doesn't exist **"
        for ob in all_obs.values():
            obs_list.append(ob.__str__())
        obs_str = str(obs_list)

        with patch("sys.stdout", new=StringIO()) as f2:
            HBNBCommand().onecmd("all")
            self.assertEqual(obs_str, f2.getvalue()[:-1])

        spec_obs_list = []
        for ob in all_obs.values():
            if ob.to_dict()["__class__"] == "User":
                spec_obs_list.append(ob.__str__())
        obs_spec_str = str(spec_obs_list)

        with patch("sys.stdout", new=StringIO()) as f2:
            HBNBCommand().onecmd("all User")
            self.assertEqual(obs_spec_str, f2.getvalue()[:-1])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all Vashow")
            self.assertEqual(error, f.getvalue()[:-1])

    def test_update_errors_and_normal(self):
        """
        Testing do_update for all cases seeing whether correct errors displayed
        trying edge cases and seeing whether the changes are in the JSON file
        And testing whether it changes existing attribute values
        and also if it can add attributes to existing instances
        Usage: update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        class_missing = "** class name missing **"
        id_missing = "** instance id missing **"
        instance_error = "** no instance found **"
        attribute_name_missing = "** attribute name missing **"
        class_error = "** class doesn't exist **"
        value_missing = "** value missing **"

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            identity = f.getvalue()[:-1]

        all_obs = storage.all()
        all_obs[f"User.{identity}"].first_name = "Jackline"
        all_obs[f"User.{identity}"].last_name = "Muriuki"
        all_obs[f"User.{identity}"].number = "42"

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue()[:-1], class_missing)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            self.assertEqual(f.getvalue()[:-1], id_missing)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update User 123-123-12312")
            self.assertEqual(f.getvalue()[:-1], instance_error)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update Kendi 123-123-12312")
            self.assertEqual(f.getvalue()[:-1], class_error)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {identity}")
            self.assertEqual(f.getvalue()[:-1], attribute_name_missing)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {identity} first_name")
            self.assertEqual(f.getvalue()[:-1], value_missing)

        HBNBCommand().onecmd(f'update User {identity} first_name "Muriuki"')
        all_obs = storage.all()
        changed_name = all_obs[f"User.{identity}"].first_name
        self.assertEqual(changed_name, "Muriuki")

        HBNBCommand().onecmd(f'update User {identity} last_name "Kendi"')
        all_obs = storage.all()
        changed_name = all_obs[f"User.{identity}"].last_name
        self.assertEqual(changed_name, "Kendi")

        HBNBCommand().onecmd(f'update User {identity} number 2')
        all_obs = storage.all()
        changed_num = all_obs[f"User.{identity}"].number
        self.assertEqual(changed_num, 2)

    def test_update_add_attributes(self):
        """
        Test whether do_update() can add attributes to an instance
        and whether they retain their type
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            identity = f.getvalue()[:-1]

        all_obs = storage.all()
        HBNBCommand().onecmd(f'update User {identity} "key" "value"')
        added_attribute = all_obs[f"User.{identity}"].key
        self.assertEqual(added_attribute, "value")
        self.assertIsInstance(added_attribute, str)

        HBNBCommand().onecmd(f'update User {identity} "num" 42')
        added_attribute = all_obs[f"User.{identity}"].num
        self.assertEqual(added_attribute, 42)
        self.assertIsInstance(added_attribute, int)

        HBNBCommand().onecmd(f'update User {identity} "flt" 42.42')
        added_attribute = all_obs[f"User.{identity}"].flt
        self.assertEqual(added_attribute, 42.42)
        self.assertIsInstance(added_attribute, float)

    def test_dot_all(self):
        """
        Tests for the all.() func when passed into the console
        And whether it performs the same error checks as: all <class name>
        Usage <class name>.all()
        """
        storage.reload()
        all_obs = storage.all()
        error = "** class doesn't exist **"
        spec_obs_list = []
        for ob in all_obs.values():
            if ob.to_dict()["__class__"] == "BaseModel":
                spec_obs_list.append(ob.__str__())
        obs_spec_str = str(spec_obs_list)

        with patch("sys.stdout", new=StringIO()) as f2:
            HBNBCommand().onecmd("BaseModel.all()")
            self.assertEqual(obs_spec_str, f2.getvalue()[:-1])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Kendi.all()")
            self.assertEqual(error, f.getvalue()[:-1])

    def test_dot_count(self):
        """
        Testing that count() is able to retrieve number of
        instances and performs the necesarry error checks
        Usage: <class name>.count()
        """
        all_obs = storage.all()
        num = 0
        cls = "User"
        error = "** class doesn't exist **"

        for ob in all_obs.values():
            if ob.to_dict()["__class__"] == cls:
                num += 1
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls}.count()")
            self.assertEqual(str(num), f.getvalue()[:-1])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"create {cls}")
            identity = f.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as num:
            HBNBCommand().onecmd(f"{cls}.count()")
            number = int(num.getvalue()[:-1])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"{cls}.destroy({identity})")
            HBNBCommand().onecmd(f"{cls}.count()")
            new_num = int(f.getvalue()[:-1])
            self.assertEqual(number-1, new_num)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Kendi.count()")
            self.assertEqual(error, f.getvalue()[:-1])

    def test_dot_show(self):
        """
        Testing to see if <class name>.show(<id>) behaves
        same as show <class name> <id>
        """
        instance_error = "** no instance found **"
        class_error = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as newId:
            HBNBCommand().onecmd("create User")
            identity = newId.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as show_alone:
            HBNBCommand().onecmd(f"show User {identity}")

        with patch("sys.stdout", new=StringIO()) as dot_show:
            HBNBCommand().onecmd(f'User.show({identity})')
            self.assertEqual(dot_show.getvalue(), show_alone.getvalue())

        with patch("sys.stdout", new=StringIO()) as dot_showq:
            HBNBCommand().onecmd(f'User.show("{identity}")')
            self.assertEqual(dot_showq.getvalue(), show_alone.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.show(1234-1234-123)")
            self.assertEqual(instance_error, f.getvalue()[:-1])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Vashow.show(1234-1234-123)")
            self.assertEqual(class_error, f.getvalue()[:-1])

    def test_dot_destroy(self):
        """
        Testing to see if <class name>.destroy(<id>) behaves
        same as destroy <class name> <id>
        """
        instance_error = "** no instance found **"
        class_error = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as newId:
            HBNBCommand().onecmd("create User")
            identity0 = newId.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as newId:
            HBNBCommand().onecmd("create User")
            identity1 = newId.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as show:
            HBNBCommand().onecmd(f"show User {identity0}")
            self.assertNotEqual(show.getvalue()[:-1], instance_error)

        HBNBCommand().onecmd(f"User.destroy({identity0})")

        with patch("sys.stdout", new=StringIO()) as show:
            HBNBCommand().onecmd(f"show User {identity0}")
            self.assertEqual(show.getvalue()[:-1], instance_error)

        with patch("sys.stdout", new=StringIO()) as dot_show:
            HBNBCommand().onecmd(f'User.show({identity1})')
            self.assertNotEqual(dot_show.getvalue()[:-1], instance_error)

        HBNBCommand().onecmd(f'User.destroy("{identity1}")')

        with patch("sys.stdout", new=StringIO()) as dot_showq:
            HBNBCommand().onecmd(f'User.show("{identity1}")')
            self.assertEqual(dot_showq.getvalue()[:-1], instance_error)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy(1234-1234-123)")
            self.assertEqual(instance_error, f.getvalue()[:-1])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Vashow.destroy(1234-1234-123)")
            self.assertEqual(class_error, f.getvalue()[:-1])

    def test_dot_update(self):
        """
        Testing if
        <class name>.update(<id>, <attribute>, <value>)
        works same as
        update <class name> <id> <attribute> <value>
        """
        id_missing = "** instance id missing **"
        instance_error = "** no instance found **"
        attribute_name_missing = "** attribute name missing **"
        class_error = "** class doesn't exist **"
        value_missing = "** value missing **"

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            identity = f.getvalue()[:-1]

        all_obs = storage.all()
        all_obs[f"User.{identity}"].first_name = "Jackline"
        all_obs[f"User.{identity}"].last_name = "Muriuki"
        all_obs[f"User.{identity}"].number = "42"

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.update()")
            self.assertEqual(f.getvalue()[:-1], id_missing)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd('User.update("123-123-12312")')
            self.assertEqual(f.getvalue()[:-1], instance_error)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd('Kendi.update("123-123-12312")')
            self.assertEqual(f.getvalue()[:-1], class_error)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f'User.update("{identity}")')
            self.assertEqual(f.getvalue()[:-1], attribute_name_missing)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f'User.update("{identity}", "first_name")')
            self.assertEqual(f.getvalue()[:-1], value_missing)

        HBNBCommand().onecmd(f'User.update("{identity}", "first_name"\
                             , "Muriuki")')
        all_obs = storage.all()
        changed_name = all_obs[f"User.{identity}"].first_name
        self.assertEqual(changed_name, "Muriuki")

        HBNBCommand().onecmd(f'User.update("{identity}"\
                             , "last_name", "Kendi")')
        all_obs = storage.all()
        changed_name = all_obs[f"User.{identity}"].last_name
        self.assertEqual(changed_name, "Kendi")

        HBNBCommand().onecmd(f'User.update("{identity}", "number", 2)')
        all_obs = storage.all()
        changed_num = all_obs[f"User.{identity}"].number
        self.assertEqual(changed_num, 2)

    def test_update_add_attributes(self):
        """
        Test whether do_update() can add attributes to an instance
        and whether they retain their type
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            identity = f.getvalue()[:-1]

        all_obs = storage.all()
        HBNBCommand().onecmd(f'User.update({identity}, key, "value")')
        added_attribute = all_obs[f"User.{identity}"].key
        self.assertEqual(added_attribute, "value")
        self.assertIsInstance(added_attribute, str)

        HBNBCommand().onecmd(f'User.update("{identity}", num, 42)')
        added_attribute = all_obs[f"User.{identity}"].num
        self.assertEqual(added_attribute, 42)
        self.assertIsInstance(added_attribute, int)

        HBNBCommand().onecmd(f'User.update({identity}, "flt", 42.42)')
        added_attribute = all_obs[f"User.{identity}"].flt
        self.assertEqual(added_attribute, 42.42)
        self.assertIsInstance(added_attribute, float)
