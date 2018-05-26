#!/usr/bin/python3
"""
module that imports the function def add(a, b)
"""


if __name__ == '__main__':
    from add_4 import add
    a, b = 1, 2
    print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
