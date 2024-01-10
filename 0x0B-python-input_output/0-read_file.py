#!/usr/bin/python3
"""difine read_file function"""


def read_file(filename=""):
    """reads a filename with  UTF-8"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
