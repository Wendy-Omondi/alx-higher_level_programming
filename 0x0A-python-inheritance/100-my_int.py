#!/usr/bin/python3
"""Defines a class named MyInt"""


class MyInt(int):
    """
    A class named MyInt
    """

    def __eq__(self, other):
        """realigns eq builtin"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """realigns ne builtin"""
        return int.__eq__(self, other)
