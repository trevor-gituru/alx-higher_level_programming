#!/usr/bin/python3
"""
Contains the append_write function
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    Args:
        filename:   The name of file
        text:   The string to append to file
    return:
        the number of characters added:
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
