#!/usr/bin/python3
"""
module: 2-square
defines a class Square
"""


class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter function to retrieve __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter function to set the __size"""

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """retrieves position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for setting position"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the current square area"""
        return (self.size ** 2)

    def my_print(self):
        """prints the square with # character"""
        if self.size == 0:
            print("")
        else:
            print('\n' * self.position[1])
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
