#!/usr/bin/python3
"""This module defines the write_file function"""


def write_file(filename="", text=""):
    """Return the JSON representation of an object
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
