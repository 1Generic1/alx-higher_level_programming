#!/usr/bin/python3
""" function that reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """ reads file
    Args:
    filename: filename
    """
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            print(file.read(), end="")
    except FileNotFoundError:
        pass
