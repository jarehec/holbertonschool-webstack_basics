#!/usr/bin/python3
"""
module containing add_integer function
"""


def add_integer(a, b):
    """
    adds two integers or floats
    @a: integer or float
    @b: integer or float
    """
    if a.__class__ is not int and a.__class__ is not float:
        raise TypeError('a must be an integer')
    if b.__class__ is not int and b.__class__ is not float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
