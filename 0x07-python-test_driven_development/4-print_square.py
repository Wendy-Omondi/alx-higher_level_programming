#!/usr/bin/python3
"""prints a square with the character #.
"""


def print_square(size):
    """prints a square.
    """
    if type(size) != int or size != size:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        for row in range(size):
            for column in range(size):
                print("#", end="")
            print()
