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

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        try:
            return json.loads(json_string)
        except json.JSONDecodeError:
            return []

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file and return a list of instances."""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
        except FileNotFoundError:
            return []
        dict_list = cls.from_json_string(json_string)
        instances = [cls.create(**d) for d in dict_list]
        return instances

