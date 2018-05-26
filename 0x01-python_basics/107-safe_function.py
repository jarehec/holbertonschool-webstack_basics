#!/usr/bin/python3
"""
module containing safe_function function
"""
from sys import stderr


def safe_function(fct, *args):
    """
    executes a function safely
    """
    try:
        return fct(*args)
    except Exception as e:
        print('Exception: {}'.format(e), file=stderr)
        return None
