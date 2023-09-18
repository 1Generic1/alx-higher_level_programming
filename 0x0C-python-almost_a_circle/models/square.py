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
    
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the Square with arguments.

        Args:
            *args: Positional arguments in the following order:
                1st argument: id attribute
                2nd argument: size attribute
                3rd argument: x attribute
                4th argument: y attribute
            **kwargs: Keyword arguments for any attribute.
        """ 
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return a dictionary representation of the Square."""
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }
    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
