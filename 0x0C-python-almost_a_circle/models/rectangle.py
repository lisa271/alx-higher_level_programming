#!/usr/bin/python3
# rectangle.py
from models.base import Base


class Rectangle(Base):
    """
    A class representing a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method for the Rectangle class

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): The x coordinate of the rectangle (optional, defaults to 0)
            y (int): The y coordinate of the rectangle (optional, defaults to 0)
            id (int): The id of the rectangle (optional)

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute

        Args:
            value (int): The value to set for the width attribute

        Raises:
            ValueError: If value is not an integer or if value is less than or equal to 0

        """
        if not isinstance(value, int):
            raise ValueError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute

        Args:
            value (int): The value to set for the height attribute

        Raises:
            ValueError: If value is not an integer or if value is less than or equal to 0

        """
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x attribute

        Args:
            value (int): The value to set for the x attribute

        Raises:
            ValueError: If value is not an integer or if value is less than 0

        """
        if not isinstance(value, int):
            raise ValueError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y attribute

        Args:
            value (int): The value to set for the y attribute

        Raises:
            ValueError: If value is not an integer or if value is less than 0

        """
        if not isinstance(value, int):
            raise ValueError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
