#!/usr/bin/python3
""" function that writes a string to a text file (UTF8) and
    returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file in UTF-8 encoding and
    returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters successfully
        written to the file. Returns 0 if an error occurs.
    """

    try:
        with open(filename, mode="w", encoding="utf-8") as file:
            num_chars_written = file.write(text)
        return num_chars_written
    except Exception as e:
        return 0
