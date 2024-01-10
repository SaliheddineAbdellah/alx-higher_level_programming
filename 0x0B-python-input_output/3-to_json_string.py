#!/usr/bin/python3
"""defining to_json_string with 1 arg"""


import json


def to_json_string(my_obj):
    """returns the JSON representation of an object"""
    return json.dumps(my_obj)
