#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """A class named Square
    attribute1 (size): size of square
    """

    def __init__(self, size=0):
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

     def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size > 0:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
