#!/usr/bin/python3
"""
Module: 2-square
Defines a class Square.
"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Getter function to retrieve __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function to set the __size"""

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns the current square area"""
        return (self.size ** 2)

    def my_print(self):
        """prints the square with # character"""
        if self.size is 0:
            print("")
        else:
            for i in range(self.size):
                print("#" * self.size)
            print()
