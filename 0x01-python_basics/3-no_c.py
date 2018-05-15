#!/usr/bin/python3
"""
module containing no_c function
"""


def no_c(str):
    """
    removes all c and C of a string and return the new string
    @str: string
    Return: new string
    """
    return ''.join([i for i in str if i != 'c' and i != 'C'])
