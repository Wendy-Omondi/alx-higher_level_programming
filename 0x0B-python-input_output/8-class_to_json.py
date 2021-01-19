#!/usr/bin/python3
"""This module creates an Object from a JSON file"""


import json


def load_from_json_file(filename):
    """returns the dictionary description with simple data structure
       (list, dictionary, string, integer and boolean)
       for JSON serialization of an object
    """
    with open(filename, encoding='utf-8') as file:
        return json.loads(file.read())
