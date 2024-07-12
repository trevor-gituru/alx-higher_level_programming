#!/usr/bin/python3
"""
Contains a Rectangle subclass, class square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""
    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
