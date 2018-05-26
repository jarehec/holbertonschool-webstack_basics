#!/usr/bin/python3
"""
module containing best_score function
"""


def best_score(my_dict):
    """
    returns a key with the biggest integer value
    @my_dict: dictionary with integer values
    """
    if my_dict is not None:
        val = max(my_dict.values())
        for k, v in my_dict.items():
            if v == val:
                return k
