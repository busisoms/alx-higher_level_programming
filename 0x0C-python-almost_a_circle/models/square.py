#!/usr/bin/python3
from models.rectangle import Rectangle
"""
defines class Square that inherits from Rectangle
"""


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square.
        y (int): The y-coordinate of the square.
        id (int): The identifier for the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): Optional. The identifier for the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str: String representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """int: Getter for the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square.

        Args:
            value (int): The size value to set.

        Returns:
            int: The size value.
        """
        self.width = value
        self.height = value
        return value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Notes:
            If args is not empty, update attributes with positional arguments.
            Otherwise, update attributes with keyword arguments.
        """
        if args:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """
        Convert the square attributes to a dictionary.

        Returns:
            dict: A dictionary representation of the square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            }
