#!/usr/bin/python3
"""This module defines the read_lines function"""


def read_lines(filename="", nb_lines=0):
    """appends a string at the end of a text file (UTF8)
       and returns the number of characters added
    """
    with open(filename, encoding='utf-8') as file:
        if nb_lines <= 0:
            for line in file:
                print(line, end="")
        else:
            for line in range(nb_lines):
                print(file.readline(), end="")
