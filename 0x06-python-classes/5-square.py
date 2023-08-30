#!/usr/bin/python3
""" a class Square that defines a square """


class Square:
    """ A class Square that defines a square.
    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
