#!/usr/bin/python3
"""Singly Linked List Module"""
import sys


def sorted_insert(self, value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
