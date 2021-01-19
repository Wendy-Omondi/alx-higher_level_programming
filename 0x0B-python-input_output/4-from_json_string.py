#!/usr/bin/python3
"""This module defines the append_write function"""


def append_write(filename="", text=""):
    """returns an object (Python data structure)
       represented by a JSON string
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
