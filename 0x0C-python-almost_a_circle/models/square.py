#!/usr/bin/python3
""" class Square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square (same for width and height).
            x (int): The x-coordinate of the square's position (default is 0).
            y (int): The y-coordinate of the square's position (default is 0).
            id (int): The unique ID of the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
