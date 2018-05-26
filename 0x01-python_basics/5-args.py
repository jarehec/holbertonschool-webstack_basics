#!/usr/bin/python3
"""
prints the number of and the list of its arguments
"""
from sys import argv


if __name__ == '__main__':
    if len(argv) < 2:
        print('0 arguments.')
    else:
        print('{}'.format(len(argv) - 1), end=' ')
        print('{}:'.format('arguments' if len(argv) > 2 else 'argument'))
        [print('{}: {}'.format(i, argv[i])) for i in range(1, len(argv))]
