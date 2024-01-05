#!/usr/bin/python3
""" Defining a locked class"""

class Lockedclass:
    """
    Prevent usr from instantiating new lockedclass attributes
    for anything but attribute called 'first_name'
    """

    __slots__ = ["first_name"]
