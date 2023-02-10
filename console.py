#!/usr/bin/python3
"""Console module that is entry point of command
    interpreter
"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
