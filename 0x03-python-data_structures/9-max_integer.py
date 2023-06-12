#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        my_list.sort()
        max = my_list[-1]
    return max
