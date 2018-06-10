#!/usr/bin/python3
"""
script that displays the value of the variable X-Request-Id from a given url
"""
import sys
from requests import get

if __name__ == '__main__':
    res = get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
