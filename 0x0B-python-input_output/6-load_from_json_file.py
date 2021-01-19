#!/usr/bin/python3
"""This module defines the to_json_string function"""


import json


def from_json_string(my_str):
    """creates an Object from a “JSON file”
    """
    return json.loads(my_str)
