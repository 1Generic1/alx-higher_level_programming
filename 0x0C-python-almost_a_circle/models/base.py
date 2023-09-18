#!/usr/bin/python3
""" the base of the project """
import json


class Base:
    """Initialize a Base instance with a unique ID.

        Args:
            id (int): The ID to assign to the instance.
            If None, a new ID will be generated.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with a unique ID.

        Args:
            id (int): The ID to assign to the instance.
            If None, a new ID will be generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list of dict): List of dictionaries to convert to JSON.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        class_name = cls.__name__
        filename = f"{class_name}.json"
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)
        with open(filename, 'w') as file:
            file.write(json_string)
