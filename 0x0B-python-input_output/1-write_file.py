#!/usr/bin/python3
"""This module defines the number_of_lines function"""


def write_file(filename="", text=""):
    """Returns the number of lines of a text file
    """
    i = 0
    with open(filename, encoding='utf-8') as file:
        for text in file:
            i += 1
        return i
