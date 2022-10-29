#!/usr/bin/python3
"""contains the entry point of the command interpreter:"""
import cmd
import json
import re
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place


class HBNBCommand(cmd.Cmd):
    new_storage = FileStorage()
    new_storage.reload()
    prompt = "(hbnb) "
    __allowed_cls = ["BaseModel", "FileStorage", "User",
                     "Place", "City", "State", "Amenity", "Review"]
    __methods = ["all", "update", "destroy", "show", "count"]

    def do_quit(self, line):
        """Exits the programme"""
        return True

    def do_EOF(self, line):
        """Signal to exit the programme"""
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel
        """
        if line:
            if line in HBNBCommand.__allowed_cls:
                new_instance = eval(line)()
                new_instance.save()
                print(new_instance.id)

            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Prints the string representation of an instance based
        on the class name and id. Ex: $ show BaseModel 1234-1234-1234
        """
        parsed_line = line.split(" ")
        if (len(parsed_line) >= 1) and (len(line) > 0):
            cls = parsed_line[0]
        else:
            print("** class name missing **")
            return
        if cls not in HBNBCommand.__allowed_cls:
            print("** class doesn't exist **")
            return
        if (len(parsed_line) == 2):
            identity = parsed_line[1]
        elif (len(parsed_line) == 1):
            print("** instance id missing **")
            return
        else:
            print(f"*** Unknown syntax: {line}")
            return

        all_objects = HBNBCommand.new_storage.all()
        parsed_list = [cls, identity]
        parsed_name = ".".join(parsed_list)
        if parsed_name in all_objects.keys():
            print(all_objects[parsed_name])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        parsed_line = line.split(" ")
        if (len(parsed_line) >= 1) and (len(line) > 0):
            cls = parsed_line[0]
        else:
            print("** class name missing **")
            return
        if cls not in HBNBCommand.__allowed_cls:
            print("** class doesn't exist **")
            return
        if (len(parsed_line) == 2):
            identity = parsed_line[1]
        elif (len(parsed_line) == 1):
            print("** instance id missing **")
            return
        else:
            print(f"*** Unknown syntax: {line}")
            return
        all_objects = HBNBCommand.new_storage.all()

        for key, value in all_objects.items():
            if identity == value.id:
                del all_objects[key]
                HBNBCommand.new_storage.save()
                return
        print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based on the class name or if no class name is provided
        Prints all instances. See usage below
        Ex: $ all BaseModel or $ all
        """
        if (line and (len(line) > 0)):
            parsed_line = line.split(" ")
        else:
            output_list = []
            objects = HBNBCommand.new_storage.all()
            for obj in objects.values():
                output_list.append(obj.__str__())
            print(output_list)
            return

        if (len(parsed_line) > 1):
            print(f"*** Unknown syntax: {line}")
            return

        cls = parsed_line[0]
        if cls in HBNBCommand.__allowed_cls:
            objects = HBNBCommand.new_storage.all()
            output_list = []
            for value in objects.values():
                if (value.to_dict()["__class__"]) == cls:
                    output_list.append(value.__str__())
            print(output_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        if (len(line) == 0):
            print("** class name missing **")
            return

        quote_match = re.search(r'"', line)
        if quote_match is not None:
            first_part = re.split(r' ', (line[:quote_match.span()[0]]).strip())
            print(f"First_part list: {first_part}")
            quote_match1 = re.search(r'"', line[quote_match.span()[1]:])
            num = quote_match.span()[0]
            if quote_match1 is None:
                print(f"*** Unknown syntax: {line}")
                return
            num1 = quote_match1.span()[1]
            last_part = [line[num:num+num1+1]]
            parsed_line = first_part + last_part
        else:
            parsed_line = line.split(" ")

        all_obs = HBNBCommand.new_storage.all()
        cls = parsed_line[0]
        if cls not in HBNBCommand.__allowed_cls:
            print("** class doesn't exist **")
            return
        if (len(parsed_line) < 2):
            print("** instance id missing **")
            return
        obj_dict = {}
        identity = parsed_line[1]
        for key, obj in all_obs.items():
            obj_dict[key] = obj.to_dict()

        parsed_name = [cls, identity]
        name = ".".join(parsed_name)
        if name not in obj_dict.keys():
            print("** no instance found **")
            return
        if (len(parsed_line) < 3):
            print("** attribute name missing **")
            return
        attribute = parsed_line[2]
        attributes = []
        if attribute in ["id", "updated_at", "created_at"]:
            print("Cannot update those attributes")
            return
        for value in obj_dict.values():
            for key in value.keys():
                if key not in ["id", "updated_at", "created_at"]:
                    attributes.append(key)
        if attribute not in attributes:
            print("** Attribute doesn't exist **")
            return
        else:
            if (len(parsed_line) < 4):
                print("** value missing **")
                return
            else:
                att_val = eval(parsed_line[3])
                setattr(all_obs[name], attribute, att_val)
                HBNBCommand.new_storage.save()

    def count(self, cls_name):
        """
        retrieve the number of instances of a class:
        <class name>.count()
        """
        obs = HBNBCommand.new_storage.all()
        count = 0
        for ob in obs.values():
            if (cls_name == ob.to_dict()["__class__"]):
                count += 1

        print(count)

    def default(self, line):
        """
        Defines what happens if the argument passed is not recognized
        """
        line_list = re.split(r'\.', line, 1)
        if (len(line_list) <= 1):
            print(f"*** Unknown syntax: {line}")
            return

        model = line_list[0]
        if model not in HBNBCommand.__allowed_cls:
            print("** class doesn't exist **")
            return

        command = line_list[1]
        patikana = re.search(r'\(', command)
        patikana3 = re.search(r'\)', command)
        if patikana3 is None:
            print(f"*** Unknown syntax: {line}")
            return

        action = command[:patikana.span()[0]]

        if action not in HBNBCommand.__methods:
            print(f"*** Unknown syntax: {line}")
            return

        arguments = command[patikana.span()[1]:-1]
        if action == "all":
            if len(arguments) > 0:
                print(f"*** Unknown syntax: {line}")
                return
            self.do_all(model)
        if action == "count":
            if len(arguments) > 0:
                print(f"*** Unknown syntax: {line}")
                return
            self.count(model)

        if action == "show":
            mini_arg = arguments.split(", ")
            if (len(mini_arg) > 1) and (len(arguments) > 0):
                print(f"*** Unknown syntax: {line}")
                return
            elif (len(arguments) == 0):
                print("** instance id missing **")
                return
            self.do_show(model + " " + arguments[1:-1])

        if action == "destroy":
            mini_arg = arguments.split(", ")
            if (len(mini_arg) > 1) and (len(arguments) > 0):
                print(f"*** Unknown syntax: {line}")
                return
            elif (len(arguments) == 0):
                print("** instance id missing **")
                return
            self.do_destroy(model + " " + arguments[1:-1])
        if action == "update":
            patikana2 = re.search(r'\{', arguments)
            if patikana2 is not None:
                identity = arguments[1:patikana2.span()[0] - 3]
                dict_json = arguments[patikana2.span()[1] - 1:]
                att_dict = eval(dict_json)
                for attr, value in att_dict.items():
                    if type(value) == str:
                        self.do_update(model + " " + identity + " "
                                       + attr + " " + '"' + value + '"')
                    else:
                        self.do_update(model + " " + identity + " "
                                       + attr + " " + str(value))
                return
            else:
                mini_arg = arguments.split(", ")
                if (len(mini_arg) == 0):
                    print("** instance id missing **")
                    return
                if len(mini_arg) != 3:
                    print(f"*** Unknown syntax: {line}")
                    return
                identity = mini_arg[0]
                attr = mini_arg[1]
                value = mini_arg[2]
                parse_line = model + " " + identity[1:-1] + " " + attr[1:-1]\
                    + " " + value
                self.do_update(parse_line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
