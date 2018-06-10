#!/usr/bin/python3
"""
script that sends a POST request to the passed url
"""
import sys
from requests import post

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    res = post(url=url, data={'email': email})
    print(res.text)
