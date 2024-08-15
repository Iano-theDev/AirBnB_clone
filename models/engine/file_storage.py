"""The file storage module
"""
import json
import os
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


class FileStorage:
    """The file starage class
    handles sotorage of files to json and reading from json to dict"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects to obj and with with obj classname.id"""
        if obj is not None:
            className = obj.__class__.__name__
            id = obj.id
            key = str(className) + "." + str(id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objjects to the JSON file (path) __file_path"""
        # print(f'[__objects is]:{self.__objects}')
        dict_to_save = {}
        for key, value in self.__objects.items():
            dict_to_save[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(dict_to_save, file)

    def reload(self):
        """deserializes to json file to __objects only if the JSON file exists.
        No exception is raised if the file doesn't exist"""
        PATH = self.__file_path
        loaded_dict = {}
        if os.path.exists(PATH):
            with open(PATH, 'r') as file:
                loaded_dict = json.load(file)
            for key, value in loaded_dict.items():
                objClass = classes[value["__class__"]]
                self.__objects[key] = objClass(**value)
        else:
            pass
