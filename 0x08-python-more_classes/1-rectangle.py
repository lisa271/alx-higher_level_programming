#!/usr/bin/python3

"""class rectangle with attributes"""


class Rectangle:
    """a class of rectangle"""
    
    def __init__(self, width=0, height=0):
        """initialising the rectangle class
        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """get/set width of the rectangle"""
        return self._width
        
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """get/set height of the rectangle"""
        return self._height

        
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
