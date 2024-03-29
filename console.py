#!/usr/bin/python3
"""Defines the HbnB console."""
import cmd
import re
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage
from models.base_model import BaseModel


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBNB command interpreter.

    Attributes:
        prompt(str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def default(self, arg):
        """Default behaviour for cmd module when input is invalid."""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg_1 = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_1[1])
            if match is not None:
                command = [arg_1[1][:match.span()[0]], match.group(1)]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(arg_1[0], command[1])
                    return arg_dict[command[0]](call)

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print()  # print a new line before exiting
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        arg_1 = parse(arg)
        if len(arg_1) == 0:
            print("** class name missing **")
        elif arg_1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_1[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        arg_1 = parse(arg)
        obj_dict = storage.all()
        if len(arg_1) == 0:
            print("** class name missing **")
        elif arg_1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_1[0], arg_1[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_1[0], arg_1[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        arg_1 = parse(arg)
        obj_dict = storage.all()
        if len(arg_1) == 0:
            print("** class name missing **")
        elif arg_1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_1[0], arg_1[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_1[0], arg_1[1])]
        storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        arg_1 = parse(arg)
        if len(arg_1) > 0 and arg_1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj1 = []
            for obj in storage.all().values():
                if len(arg_1) > 0 and arg_1[0] == obj.__class__.__name__:
                    obj1.append(obj.__str__())
                elif len(arg_1) == 0:
                    obj1.append(obj.__str__())
                    print(obj1)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        arg_1 = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg_1[0] == obj.__class__.__name__:
                count += 1
                print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <attribute_name>, <attribute_value>) or
        <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        arg_1 = parse(arg)
        obj_dict = storage.all()

        if len(arg_1) == 0:
            print("** class name missing **")
            return False
        if arg_1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_1) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_1[0], arg_1[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_1) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_1) == 3:
            try:
                type(eval(arg_1[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_1) == 4:
            obj = obj_dict["{}.{}".format(arg_1[0], arg_1[1])]
            if arg_1[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_1[2]])
                obj.__dict__[arg_1[2]] = valtype(arg_1[3])
            else:
                obj.__dict__[arg_1[2]] = arg_1[3]
        elif type(eval(arg_1[2])) == dict:
            obj = obj_dict["{}.{}".format(arg_1[0], arg_1[1])]
            for k, p in eval(arg_1[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(p)
                else:
                    obj.__dict__[k] = p
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
