#!/usr/bin/python3
"""a class rectangle that defines a rectangle"""


class Rectangle:
    """A class named Rectangle
       with height and width
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        """retrieves height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height of the rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """retrieves width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle's perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """Returns the string representation of the class instance"""
        hashstring = ""
        if self.__width == 0 or self.__height == 0:
            return hashstring
        for row in range(self.__height):
            for column in range(self.__width):
                hashstring += "#"
            if row < self.__height - 1:
                hashstring += "\n"
        return hashstring
