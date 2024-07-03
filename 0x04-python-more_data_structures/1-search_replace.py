#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    a function that replaces all occurrences of
    an element by another in a new list
    """
    if my_list is not None:
        new_list = [elememt if elememt != search else replace for elememt in my_list]
        return new_list
