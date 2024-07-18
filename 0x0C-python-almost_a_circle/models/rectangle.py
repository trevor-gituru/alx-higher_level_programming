#!/usr/bin/python3
"""
model: rectangle
"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor
        width: Width of the rectangle.
        height: Height of the rectangle.
        x (defaulting to 0): x-coordinate of the rectangle.
        y (defaulting to 0): y-coordinate of the rectangle.
        id (defaulting to None): An optional identifier for the rectangle.
        """
        # Call the super class with id
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @property
    def x(self):
        """X getter"""
        return self.__x

    @property
    def y(self):
        """Y getter"""
        return self.__y

    @width.setter
    def width(self, width):
        """Width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @height.setter
    def height(self, height):
        """Height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """returns the area value"""
        return (self.height * self.width)

    def display(self):
        """prints the Rectangle instance with the character #"""
        print('\n' * self.y, end='')
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """returns string representation of an obeject"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.width, self.height)

    def update(self, *args):
        """assigns an argument to each attribute"""
        attr_list = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, attr_list[i], args[i])

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        # rectangle_dict = {}
        # rectangle_dict["id"] = self.id
        # rectangle_dict["width"] = self.width
        # rectangle_dict["height"] = self.height
        # rectangle_dict["x"] = self.x
        # rectangle_dict["y"] = self.y
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
