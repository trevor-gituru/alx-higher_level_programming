#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_int = my_list[0]
        for i in range(1, len(my_list)):
            max_int = my_list[i] if max_int < my_list[i] else max_int
        return max_int
