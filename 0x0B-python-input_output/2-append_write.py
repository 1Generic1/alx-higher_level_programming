#!/usr/bin/python3
""" function that appends a string at the end of a text file (UTF8) and
    returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file in UTF-8 encoding and
    returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters successfully added to the file.
        Returns 0 if an error occurs.
    """

    try:
        with open(filename, mode="a", encoding="UTF8") as file:
            num_char_added = file.write(text)
        return num_char_added
    except Exception as e:
        return 0
