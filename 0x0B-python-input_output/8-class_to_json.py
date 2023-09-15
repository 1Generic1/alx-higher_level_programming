#!/usr/bin/python3
""" function that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """ function that returns the dictionary """

    if not hasattr(obj, "__dict__"):
        raise TypeError("Input is not an instance of a class")
    serialized_data = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized_data[key] = value
    return serialized_data
