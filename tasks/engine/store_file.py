#!/usr/bin/python3
"""Class for file storage"""
from tasks.functions import Task


class StoreList:
    """Stores the To-Do in a json file"""

    __file_path = "to-do.json"
    __objects = {}

    def all(self):
        """returns a dict repr of to-do list"""
        return self.__objects
    
    
