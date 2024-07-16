#!/usr/bin/python3
"""
Contains the class Student
"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dicionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        return {key: value for (key, value) in self.__dict__.items()
                if key in attrs}
