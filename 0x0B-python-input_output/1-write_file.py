#!/usr/bin/python3
"""This module defines the number_of_lines function"""


def number_of_lines(filename=""):
    """Returns the number of lines of a text file
    """
    i = 0
    with open(filename, encoding='utf-8') as file:
        for line in file:
            i += 1
        return i
