#!/usr/bin/python3
"""
script that displays your github id
"""
from requests import get
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    res = get('https://api.github.com/user', auth=HTTPBasicAuth(user, pwd))
    print(res.json().get('id'))
