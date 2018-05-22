#!/usr/bin/python3
"""
module containing print_diagonal function
"""


def print_diagonal(n):
    """
    draws a diagonal line
    @n: integer:q
    """
    if n <= 0:
        print('\n')
    else:
        [print(' ' * i + '\\') for i in range(n)]
