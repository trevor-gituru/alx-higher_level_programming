#!/usr/bin/python3
""" Contains a function that prints a square

args:
    size - size length of the square
"""


def print_square(size):
    """
    prints a square with the character #
    """
    if type(size) is not int or (isinstance(size, float) and size < 0):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
