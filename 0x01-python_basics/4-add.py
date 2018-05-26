#!/usr/bin/python3
"""
module that imports the function def add(a, b)
"""
from add_4 import add


if __name__ == '__main__':
    a = 1
    b = 2
    print('{} + {} = {}'.format(a, b, add(a, b)))
