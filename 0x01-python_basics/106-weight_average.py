#!/usr/bin/python3
"""
module containing weight_average function
"""


def weight_average(my_list=[]):
    """
    returns the weighted average of all integers tuple
    @my_list: list of tuples (<score>, <weight>)
    """
    if len(my_list) == 0:
        return 0
    lval = sum([i[0] * i[1] for i in my_list])
    rval = sum([i[1] for i in my_list])
    return lval / rval
