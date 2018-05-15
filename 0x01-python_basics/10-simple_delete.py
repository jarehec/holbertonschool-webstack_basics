#!/usr/bin/python3
"""
module containing simple_delete function
"""


def simple_delete(my_dict, key=""):
    """
    deletes a key in a dictionary
    @my_dict: a dictionary
    @key: string
    """
    if my_dict.get(key) is not None:
        del my_dict[key]
    return my_dict
