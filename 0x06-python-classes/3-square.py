#!/usr/bin/python3
"""
module: 2-square
Defines a class Square
"""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        self.__size = size

        if type(self.__size) is not int:
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the current square area."""
        return (self.__size ** 2)
