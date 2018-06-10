#!/usr/bin/python3
"""
script that displays the body of the response of a given url
"""
import sys
from requests import get

if __name__ == '__main__':
    res = get(sys.argv[1])
    if res.status_code >= 400:
        print('Error code:', res.status_code)
    else:
        print(res.text)
