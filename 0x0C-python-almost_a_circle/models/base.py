#!/usr/bin/python3
""" the base of the project """
import json
import csv


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
            list_dictionaries (list of dict): List of
                dictionaries to convert to JSON.

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects and writes them to a CSV file.

        Args:
            cls (type): The class type (e.g., Rectangle or Square).
            list_objs (list): A list of instances to serialize and write.

        Returns:
            None

        """
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == 'Rectangle':
                header = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == 'Square':
                header = ['id', 'size', 'x', 'y']
            writer.writerow(header)
            for obj in list_objs:
                values = [getattr(obj, attr) for attr in header]
                writer.writerow(values)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes objects from a CSV file and returns them as a list.

        Args:
            cls (type): The class type (e.g., Rectangle or Square).

        Returns:
            list: A list of instances deserialized from the CSV file.

        """
        filename = f"{cls.__name__}.csv"
        list_objs = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                values = row
                if cls.__name__ == 'Rectangle':
                    id, width, height, x, y = map(int, values)
                    obj = cls(width, height, x, y, id)
                elif cls.__name__ == 'Square':
                    id, size, x, y = map(int, values)
                    obj = cls(size, x, y, id)
                list_objs.append(obj)
        return list_objs
