#!/usr/bin/python3
"""contains the entry point of the command interpreter:"""
import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenity  import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place

class HBNBCommand(cmd.Cmd):
    new_storage = FileStorage()
    new_storage.reload()
    prompt = "(hbnb) "
    allowed_cls = ["BaseModel", "FileStorage", "User",\
                "Place", "City", "State", "Amenity", "Review"] 
        
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
            if line in HBNBCommand.allowed_cls:
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
        if (len(parsed_line) >= 1):
            cls = parsed_line[0]
        else:
            print("** class name missing **")

        if (len(parsed_line) == 2):
            identity = parsed_line[1]
        elif (len(parsed_line) == 1):
            print("** instance id missing **")
        else:
            print("Too many arguements, help show, to see usage")
            return

        if cls in HBNBCommand.allowed_cls:
            HBNBCommand.new_storage.reload()
            all_objects = HBNBCommand.new_storage.all()
            parsed_list = [cls, identity]
            parsed_name = ".".join(parsed_list)
            if parsed_name in all_objects.keys():
                print(all_objects[parsed_name])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **") 
    
    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        parsed_line = line.split(" ")
        if (len(parsed_line) >= 1):
            cls = parsed_line[0]
        else:
            print("** class name missing **")

        if (len(parsed_line) == 2):
            identity = parsed_line[1]
        elif (len(parsed_line) == 1):
            print("** instance id missing **")
        else:
            print("Too many arguements, help show, to see usage")
            return

        if cls in HBNBCommand.allowed_cls:
            parsed_list = [cls, identity]
            parsed_name = ".".join(parsed_list)
            with open("file.json", "r", encoding='utf-8') as file:
                obj_dict = json.load(file)

            with open("file.json", "w", encoding='utf-8') as file:
                if parsed_name in obj_dict.keys():
                    del obj_dict[parsed_name]
                    json.dump(obj_dict, file)

                else:
                    print("** no instance found **")

        else:
            print("** class doesn't exist **") 

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        if (line and (len(line) > 0)):
            parsed_line = line.split(" ")
        else:
            objects = HBNBCommand.new_storage.all()
            for obj in objects.values():
                print(obj)
            return

        if (len(parsed_line) > 1):
            print("Invalid usage, prompt 'help all', for instructions")
            return

        cls = parsed_line[0]
        if cls in HBNBCommand.allowed_cls:
            objects = HBNBCommand.new_storage.all()
            for value in objects.values():
                if (value.to_dict()["__class__"]) == cls:
                    print(value)
        else:
            print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
