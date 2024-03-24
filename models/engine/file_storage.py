#!/usr/bin/python3
"""Defines the Filestorage class."""
import json
import importlib
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This represents an abstracted storage.

    Attributes:
        __file_path(str): The name of the file to save the objects in.
        __objects(dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)."""
        ddict = FileStorage.__objects
        obj_dict = {obj: ddict[obj].to_dict() for obj in ddict}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the json file __file_path to __objects,
        if it exists."""
        from json.decoder import JSONDecodeError
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for d in obj_dict.values():
                    cls_name = d.pop("__class__")
                    cls = getattr(importlib.import_module('models.' +
                        cls_name), cls_name)
                    obj = cls(**d)
                    self.new(obj)

        except FileNotFoundError:
            pass
        except JSONDecodeError as e:
            pass
        else:
            from models import storage  # Import storage here
            storage.new(self)
