#!/usr/bin/python3
"""
model: square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """class contructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        super().update(width=value, height=value)

    def __str__(self):
        """returns string representation of objects"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.width)

    def update(self, *args, **kwargs):
        """assigns attributes"""
        attr_list = ["id", "size", "x", "y"]
        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, attr_list[i], args[i])
        else:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        square_dict = {}
        square_dict["id"] = self.id
        square_dict["x"] = self.x
        square_dict["size"] = self.size
        square_dict["y"] = self.y
        return square_dict
