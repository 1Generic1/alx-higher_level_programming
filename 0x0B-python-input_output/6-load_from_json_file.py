#!/usr/bin/python3
""" function that creates an Object from a “JSON file" """
import json


def load_from_json_file(filename):
    """
    Loads an object from a JSON file.

    Args:
        filename (str): The name of the file containing the JSON data.

    Returns:
        object: The Python object created from the JSON data.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
