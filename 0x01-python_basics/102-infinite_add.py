#!/usr/bin/python3
"""
program that prints the result of addition of all it's arguments
"""
from sys import argv


if __name__ == '__main__':
    total = int()
    for i in range(1, len(argv)):
        total += int(argv[i])
    print(total)
