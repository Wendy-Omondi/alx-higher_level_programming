#!/usr/bin/python3
"""This module defines the to_json_string function"""


import json


def to_json_string(my_obj):
    """writes an Object to a text file, using a JSON representation
    """
    return json.dumps(my_obj)
