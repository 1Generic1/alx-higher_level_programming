#!/usr/bin/python3
""" the base of the project """


class Base:
    """Initialize a Base instance with a unique ID.

        Args:
            id (int): The ID to assign to the instance. If None, a new ID will be generated.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """Initialize a Base instance with a unique ID.

        Args:
            id (int): The ID to assign to the instance. If None, a new ID will be generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
