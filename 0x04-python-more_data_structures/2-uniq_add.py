#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is not None:
        """
        a function that adds all unique integers in a list
        """
        unique_list = set(my_list)
        unique_sum = 0
        for item in unique_list:
            unique_sum += item
        return unique_sum
