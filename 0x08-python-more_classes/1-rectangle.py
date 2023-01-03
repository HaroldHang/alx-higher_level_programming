#!/usr/bin/python3
"""A module for working with rectangles.
"""

class Rectangle:
    """Represents a 2D Polygon with 4 perpendicular sides.
    """
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle with a given width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        """Retrieves the width of this Rectangle.
        Returns:
            int: The width of this Rectangle.
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """Updates the width of this Rectangle.
        Args:
            value (int): The new width of this Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of this Rectangle.
        Returns:
            int: The height of this Rectangle.
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """Updates the height of this Rectangle.
        Args:
            value (int): The new height of this Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
