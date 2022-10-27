#!/usr/bin/python3

import cmd
import shlex
from models.base_model import BaseModel
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    allowed_classes = ["BaseModel", "User", "Review", "State",
            "Place", "City", "Amenity"]

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        if line:
            if line in HBNBCommand.allowed_classes:
                instance = eval(line)()
                instance.save()
                print(instance.id)

    def do_show(self, line):
        if line:
            words = line.split()
            if len(words) != 2:
                print("** instance id missing **")
            elif words[0] not in HBNBCommand.allowed_classes:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    if words[1] == value.id:
                        print(value)
                        return
                print("** no instance found **")
    def do_destroy(self, line):
        words = line.split()
        if not words:
            print("** class name missing **")
            return
        elif len(words) < 2:
            print("** instance id missing **")
            return
        if words[0] not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
            return
        for key, value in storage.all().items():
            if words[1] == value.id:
                del storage.all()[key]
                storage.save()
                return
    def do_all(self, line):
        split_words = shlex.split(line)
        new_list = []
        json_dict = storage.all()
        if line:
            for key in storage.all():
                if split_words[0] == key.split('.')[0]:
                    new_list.append(str(json_dict[key]))
                    print(new_list)
                else:
                    print("** class doesn't exist **")
        else:
            for key in storage.all():
                new_list.append(str(storage.all()[key]))
                print(new_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
