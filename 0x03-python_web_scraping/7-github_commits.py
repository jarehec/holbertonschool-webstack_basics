#!/usr/bin/python3
"""
script that displays 10 recent commits from github
"""
import sys
from requests import get

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    res = get('https://api.github.com/repos/{}/{}/commits'.format(
               repo, owner))
    for i in res.json()[:10]:
        print(i['sha'] + ': ' + i['commit']['author']['name'])
