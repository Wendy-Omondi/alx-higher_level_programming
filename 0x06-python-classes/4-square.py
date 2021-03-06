#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """A class named Square
    attribute1 (size): size of square
    """

    def __init__(self, size=0):
        """Initializes a new Square.
           Args:
           size (int): The size of the new square.
        """

        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
            self.__size = size

    def area(self):
        """returns the current square area"""

        return self.__size * self.__size

    @property
    def size(self):
        """Get and set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
