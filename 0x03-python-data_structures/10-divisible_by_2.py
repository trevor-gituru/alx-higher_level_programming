#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = []
    i = 0
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
        i += 1
    return bool_list
