#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1):
        return None
    copylist = my_list.copy()
    copylist.sort()
    return copylist[-1]
