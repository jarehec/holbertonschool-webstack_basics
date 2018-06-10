#!/usr/bin/python3
"""
script that sends a search request to the Star Wars API
"""
import sys
from requests import get

if __name__ == '__main__':
    res = get('https://swapi.co/api/people/?search={}'.format(sys.argv[1]))
    print('Number of result: {}'.format(res.json().get('count')))
    [print(i.get('name')) for i in res.json().get('results')]
