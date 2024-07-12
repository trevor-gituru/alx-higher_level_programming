#!/usr/bin/python3
"""
Contains the class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """derived class"""
    def __init__(self, width, height):
        """constructor"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area"""
        return self.__width * self.__height

    def __str__(self):
        """returns rectangle description"""
        return f"[Rectangle] {self.__width:d}/{self.__height:0d}"
