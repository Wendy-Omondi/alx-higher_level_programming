#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """A class named Square
    attribute1 (size): size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square.
           Args:
           size (int): The size of the new square.
        """

        self.__size = size
        self.position = position

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
