#!/usr/bin/python3
"""class rectangle with attributes"""


class Rectangle:
    """a class of rectangle"""
    
    def __init__(self, width=0, height=0):
        """initialising the rectangle class
        args width(int)
        args height(int)"""

        self.width = width
        self.height = height

        @property
        def width(self):
            return self.width
        
        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be <= 0")
            self.width = value

        @property
        def height(self):
            return self.height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be <= 0")
            self.height = value
