#!/usr/bin/python3
"""
FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
import os


class FileStorage:
    """
    Defines a `FileStorage` class that uses JSON to
    serialize and deserialize object instances and
    saves to a storage file.
    + ``__file_path``: string - path to the JSON file (ex: file.json)
    + ``__objects``: dictionary - empty but will store all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary `__objects`."""
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key
        <obj class name>.id.
        """
        from models.base_model import BaseModel
        if obj and isinstance(obj, BaseModel):
            key = type(obj).__name__ + "." + obj.id
            self.__objects.update({key: obj})

    def save(self):
        """Serializes `__objects` to the JSON file path."""
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            objects_json = {}
            for key, obj in self.__objects.items():
                objects_json.update({key: obj.to_dict()})
            json.dump(objects_json, f)
        f.close()

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file `__file_path` exists;
        otherwise, do nothing.)
        No exception should be raised if file doesn't exist.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as g:

                from models.base_model import BaseModel
                from models.user import User
                from models.city import City
                from models.place import Place
                from models.state import State
                from models.amenity import Amenity
                from models.review import Review

                content = g.read()
                objects_json = json.loads(content)
                self.__objects = {}
                for key, obj in objects_json.items():
                    name = obj["__class__"]
                    r_obj = eval("{}({})".format(name, "**obj"))
                    self.new(r_obj)
            g.close()
        else:
            pass
