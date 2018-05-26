#!/usr/bin/python3
"""
prints the alphabet, in lowercase, not followed by a new line
"""


for i in range(ord('a'), ord('z') + 1):
    if i != ord('q') and i != ord('e'):
        print('{}'.format(chr(i)), end='')
