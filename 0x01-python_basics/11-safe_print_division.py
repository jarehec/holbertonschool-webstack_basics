#!/usr/bin/python3
"""
module that contains safe_print_division function
"""


def safe_print_division(a, b):
    """
    divides 2 integers and prints the result
    @a: integer
    @b: integer
    """
    try:
        result = a / b
    except:
        result = None
    finally:
        print('Inside result: {}'.format(result))
    return result
