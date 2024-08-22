#!/usr/bin/python3
"""
0-hbtn_status.py

Task 0

This script fetches the URL https://alx-intranet.hbtn.io/status using
the urllib package and displays the response body in a specified format.

For detailed task description, requirements, and usage,
refer to the README file.
"""
from urllib.request import urlopen

url = 'https://alx-intranet.hbtn.io/status'
with urlopen(url) as response:
    content = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(content.decode('utf8')))
