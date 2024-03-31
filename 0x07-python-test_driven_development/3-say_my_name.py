#!/usr/bin/python3
"""contains a method that prints the full name

args: first_name - first name
      last_name - last name
"""


def say_my_name(first_name, last_name=""):
    """
    prints a persons full name
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print(f'My name is {first_name} {last_name}')
