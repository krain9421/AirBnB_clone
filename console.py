#!/usr/bin/python3
"""Console module that is entry point of command
    interpreter
"""
import cmd
import inspect
from models.base_model import BaseModel
from models import storage
import sys
current_module = sys.modules[__name__]
# Dictionary that will contain all the classes
class_dict = dict(inspect.getmembers(current_module))


class HBNBCommand(cmd.Cmd):
    """HBNB command processor"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing if an empty line is passed"""

    def do_create(self, name):
        """Creates a new instance of BaseModel,
            saves it to the JSON file and prints
            the id.
        """
        # Dictionary that will contain all the classes
        # class_dict = dict(inspect.getmembers(current_module))
        if not name:
            print("** class name missing **")
        elif name not in class_dict.keys():
            print("** class doesn't exist **")
        else:
            new = class_dict[name]()
            new.save()
            print(new.id)

    def do_show(self, line):
        """Prints the string representation of an
            instance based on class name and id
        """
        lines = line.split()
        try:
            name = lines[0]
        except IndexError:
            name = None

        try:
            idi = lines[1]
        except IndexError:
            idi = None

        if not name:
            print("** class name missing **")
        elif name not in class_dict.keys():
            print("** class doesn't exist **")
        elif not idi:
            print("** instance id missing **")
        else:
            d = storage.all()
            # Flag for checking if instance is found
            flag = False
            # print("File__objects\n{}".format(d))
            for key in d.keys():
                if idi == d[key]["id"]:
                    model_json = d[key]
                    temp = BaseModel(**model_json)
                    print(str(temp))
                    flag = True
            if not flag:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name
            and id (saves to JSON file)
        """
        lines = line.split()
        try:
            name = lines[0]
        except IndexError:
            name = None

        try:
            idi = lines[1]
        except IndexError:
            idi = None

        if not name:
            print("** class name missing **")
        elif name not in class_dict.keys():
            print("** class doesn't exist **")
        elif not idi:
            print("** instance id missing **")
        else:
            d = storage.all()
            flag = False
            for key in d.keys():
                if idi == d[key]["id"]:
                    d.pop(key)
                    flag = True
                    storage.save()
                    break
            if not flag:
                print("** no instance found **")

    def do_all(self, name):
        """Prints all the string representations of
            all instances based or not on class name
        """
        if not name or name in class_dict.keys():
            d = storage.all()
            list_all = []
            for key in d.keys():
                model_json = d[key]
                temp = BaseModel(**model_json)
                list_all.append(str(temp))
            print(list_all)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
