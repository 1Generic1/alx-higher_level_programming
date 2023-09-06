#!/usr/bin/python3
""" This module prints My name is <first name> <last name> """

def say_my_name(first_name, last_name=""):
    """
    prints first_name and last name

    args:
    first_name: the first name to be printed 
    last_name: the last_name to be printed. Defaults to an empty string.

    Returns: first_name and last_name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    formatted_name = "my name is {} {}".format(first_name, last_name)
    print(formatted_name)
    return formatted_name
