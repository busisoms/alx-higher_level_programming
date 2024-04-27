#!/usr/bin/python3
from models.base import Base

"""
defines Rectangle class that inheritd from Base
"""


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.

    Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
        __x (int): Horizontal position of the rectangle.
        __y (int): Vertical position of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): Horizontal position of the rectangle.
            y (int): Vertical position of the rectangle.
            id (int): Optional. The identifier for the instance.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """int: Getter for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: Getter for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """int: Getter for the horizontal position of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the horizontal position of the rectangle.

        Args:
            value (int): The horizontal position value to set.

        Raises:
            ValueError: If the value is less than 0.
        """
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: Getter for the vertical position of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the vertical position of the rectangle.

        Args:
            value (int): The vertical position value to set.

        Raises:
            ValueError: If the value is less than 0.
        """
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """Display the rectangle using '#' characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """str: String representation of the rectangle."""
        return (f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

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
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """
        Convert the rectangle attributes to a dictionary.

        Returns:
            dict: A dictionary representation of the rectangle.
        """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
