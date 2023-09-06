#!/usr/bin/python3
""" THis module prints a Square with the character # """

def print_square(size):
    """
    prints Square
    
    Args:
    size: size length  of the sqaure
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for num in range(size):
        print("#" * size)
