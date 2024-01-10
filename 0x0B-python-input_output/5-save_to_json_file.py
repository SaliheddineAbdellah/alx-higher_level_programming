#!/usr/bin/python3
"""defining save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """writes Obj to txt file using a JSON representation"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dumps(my_obj, f)
