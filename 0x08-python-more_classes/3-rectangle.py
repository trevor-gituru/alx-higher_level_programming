#!/usr/bin/python3
"""
Module: 0-rectangle
Contains the class Rectangle
Rectangle has the attributes width and height
"""


class Rectangle:
    """
    Defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes the rectangles fields"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter that retrives the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter that sets width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """Getter that retrives the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter that sets height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """Returns rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """Prints the rectanglw with #s"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rect_str = ''
        for _ in range(self.__height):
            rect_str += '#' * self.__width + '\n'
        return rect_str[:-1]
