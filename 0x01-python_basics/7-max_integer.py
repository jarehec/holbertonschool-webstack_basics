#!/usr/bin/python3
"""
module containing max_integer function
"""


def max_integer(my_list=[]):
    """
    finds the biggest integer of a list
    @my_list: list of integers
    """
    if len(my_list) == 0:
        return None
    maximum = float('-inf')
    for i in my_list:
        maximum = i if i > maximum else maximum
    return maximum
