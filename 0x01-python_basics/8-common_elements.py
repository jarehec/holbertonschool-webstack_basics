#!/usr/bin/python3
"""
module containing common_elements function
"""


def common_elements(set_1, set_2):
    """
    returns a set of common elements in two sets
    @set_1: set
    @set_2: set
    """
    return set_1.intersection(set_2)
