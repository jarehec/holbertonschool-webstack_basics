#!/usr/bin/python3
"""
module containing new_in_list function
"""


def new_in_list(my_list, idx, element):
    """
    replaces an element in a list at a specific position
    @my_list: list
    @idx: index for insertion
    @element: new data
    """
    new_list = my_list.copy()
    if idx >= 0 and idx < len(my_list):
        new_list[idx] = element
    return new_list
