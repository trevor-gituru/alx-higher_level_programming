#!/usr/bin/python3
"""
Contains the method MyList
"""


class MyList(list):
    """prints sorted list in ascending order """
    def print_sorted(self):
        print(sorted(self))
