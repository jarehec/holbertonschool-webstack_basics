#!/usr/bin/python3
"""
module containing replace_in_list function
"""


def replace_in_list(my_list, idx, element):
    """
    replaces an element of a list at a specific position
    @my_list: list
    @idx: index position
    @element: replacement value
    """
    if idx < len(my_list):
        my_list[idx] = element
    return my_list
