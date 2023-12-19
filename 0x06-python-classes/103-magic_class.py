#!/usr/bin/python3
"""Defines a MagicClass that does exactly the same as the bytecode"""

import math


class MagicClass:
    """Represents a circle"""

    def __init__(self, radius=0):
        """Initialize a magicclass
        Arg:
            radius (float or int): radius of new magicclass
        """
        self.__radius = 0
        if type(radius) in not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return area of magicclass"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return circumference of magicclass"""
        return (2 * math.pi * self.__radius)
