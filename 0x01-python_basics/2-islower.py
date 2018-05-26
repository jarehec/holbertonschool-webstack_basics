#!/usr/bin/python3
"""
module containing islower
"""


def islower(c):
    """
    checks for lowercase character
    @c: single character
    """
    return ord(c) >= ord('a') and ord(c) <= ord('z')
