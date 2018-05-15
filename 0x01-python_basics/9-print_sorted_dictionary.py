#!/usr/bin/python3
"""
module containing print_sorted_dictionary function
"""


def print_sorted_dictionary(my_dict):
    """
    prints a dictionary by ordered keys
    @my_dict: dictionary
    """
    [print('{}: {}'.format(i, my_dict[i])) for i in sorted(my_dict.keys())]
