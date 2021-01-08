#!/usr/bin/python3
"""adds two integers"""


def add_integer(a, b=98):
    if (type(a) != int and type(a) != float) or a != a:
        raise TypeError("a must be an integer")
    if (type(b) != int and type(b) != float) or b != b:
        raise TypeError("a must be an integer")
    return int(a) + int(b)
