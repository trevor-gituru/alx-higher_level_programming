#!/usr/bin/python3
"""
1-hbtn_header.py

Task 0

This script takes a URL as a command-line argument, sends a request
to the URL, and displays the value of the X-Request-Id variable found
in the header of the response.

For detailed task description and requirements, refer to the README file.
"""
from urllib.request import urlopen
from sys import argv

with urlopen(argv[1]) as response:
    res_headers = response.info()
    print(res_headers.get('X-Request-Id'))
