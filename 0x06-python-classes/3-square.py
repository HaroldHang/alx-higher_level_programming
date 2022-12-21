#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square, a 2D polygon."""

    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
    
    def area(self):
        """Area of the square."""
        return (self.__size * self.__size)
