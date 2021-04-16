#!/usr/bin/python3
"""Defines Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class named BaseGeometry
    """
    def __init__(self, width, height):
        """initializes an instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
