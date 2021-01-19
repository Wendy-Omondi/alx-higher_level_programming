#!/usr/bin/python3
"""This module creates a func that returns the dict for JSON serialization"""


def class_to_json(obj):
    """Returns the dictionary description of object
    """
    return obj.__dict__
