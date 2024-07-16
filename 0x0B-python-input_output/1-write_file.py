#!/usr/bin/python3
"""
Contains the write_file function
"""


def write_file(filename="", text=""):
    """Writes a string to text file the returns # of chars"""
    with open(filename, 'w', encoding="utf-8") as file:
        count = file.write(text)
        return count
