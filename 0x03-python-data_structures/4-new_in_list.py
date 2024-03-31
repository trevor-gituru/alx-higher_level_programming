#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None:
        list_copy = my_list.copy()

        if idx < 0 or idx > len(my_list) - 1:
            return list_copy

        list_copy[idx] = element
        return list_copy
