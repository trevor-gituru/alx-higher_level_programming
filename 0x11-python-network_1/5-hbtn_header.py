#!/usr/bin/python3
"""
5-hbtn_header.py

Task 5

This script takes a URL as a command-line argument, sends a request to the
URL, and displays the value of the `X-Request-Id` variable found in the
response header.

For detailed task description and requirements, refer to the README file.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
