#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
<<<<<<< HEAD

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
=======
    def __init__(self, width=0, height=0):
        """Initialize the new Rectangle.
>>>>>>> d165e6257c97081c4633f6a87cf0f8d13f362177
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
<<<<<<< HEAD
=======

>>>>>>> d165e6257c97081c4633f6a87cf0f8d13f362177
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width
<<<<<<< HEAD

=======
        
>>>>>>> d165e6257c97081c4633f6a87cf0f8d13f362177
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

<<<<<<< HEAD
=======
        
>>>>>>> d165e6257c97081c4633f6a87cf0f8d13f362177
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
