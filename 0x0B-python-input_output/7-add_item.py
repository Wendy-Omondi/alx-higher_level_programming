#!/usr/bin/python3
"""This module defines the save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """a script that adds all arguments to a Python list,
       and then save them to a file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
