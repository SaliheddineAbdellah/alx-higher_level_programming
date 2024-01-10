#!/usr/bin/python3
"""the class Student"""


class Student:
    """Represantation of the class student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dict representation of a Student instance"""
        return self.__dict__