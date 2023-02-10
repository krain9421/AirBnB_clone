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
        key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes `__objects` to the JSON file path"""
        with open(FileStorage.__file_path, 'w') as f:
            # content = json.dumps(FileStorage.__objects)
            # f.write(content)
            json.dump(FileStorage.__objects, f)
        f.close()

    def reload(self):
        """Deserializes the JSON file to __objects
            (only if the JSON file `__file_path` exists;
            otherwise, do nothing.)
            No exception should be raised if file doesn't exist
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as g:
                content = g.read()
                # if content != "":
                FileStorage.__objects = json.loads(content)
            g.close()
        else:
            pass
