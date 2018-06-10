#!/usr/bin/python3
"""
script that sends a POST request with a letter as a parameter
"""
import sys
from requests import post

if __name__ == '__main__':
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    res = post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        json_data = res.json()
        if len(json_data) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(json_data.get('id'), json_data.get('name')))
    except:
        print('Not a valid JSON')
