#!/usr/bin/python3
"""FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
"""
import json
import os


class FileStorage:
    """Defines a FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary `__objects`"""
        return (FileStorage.__objects)

    def new(self, obj):
        """Sets in __objects the obj with key
            <obj class name>.id
        """
        from models.base_model import BaseModel
        if obj and isinstance(obj, BaseModel):
            key = type(obj).__name__ + "." + obj.id
            # Debugging
            # print("--------DEBUGGING--------")
            # print("obj:\n{}".format(obj.to_dict()))
            # print("--------DEBUGGING--------")
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes `__objects` to the JSON file path"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            # content = json.dumps(FileStorage.__objects)
            # f.write(content)
            objects_json = {}
            for key, obj in FileStorage.__objects.items():
                objects_json[key] = obj.to_dict()
            json.dump(objects_json, f)
        f.close()

    def reload(self):
        """Deserializes the JSON file to __objects
            (only if the JSON file `__file_path` exists;
            otherwise, do nothing.)
            No exception should be raised if file doesn't exist
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as g:
                # internal import statements
                from models.base_model import BaseModel
                from models.user import User

                content = g.read()
                FileStorage.__objects = {}
                objects_json = json.loads(content)
                for key, obj in objects_json.items():
                    name = obj["__class__"]
                    r_obj = eval("{}({})".format(name, "**obj"))
                    self.new(r_obj)
            g.close()
        """else:
            pass"""
