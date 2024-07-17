#!/usr/bin/python3
"""
Contains the class Student
"""


class Student:
    """defines a student

    Args:
        first_name: Students first name
        last_name: Students last name
        age: Students age
    """
    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dicionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        return {key: value for (key, value) in self.__dict__.items()
                if key in attrs}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
