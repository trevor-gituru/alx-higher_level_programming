#!/usr/bin/python3
"""
7-error_code.py

Task 0

This script takes a URL as a command-line argument, sends a request to the
URL, and displays the body of the response. If the HTTP status code is 400
or greater, it prints: Error code: followed by the HTTP status code.

For detailed task description and requirements, refer to the README file.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    response = requests.get(url)
    status = response.status_code
    if (status >= 400):
        print("Error code: {}".format(status))
    else:
        content = response.text
        print(content)
