#!/usr/bin/python3
"""
3-error_code.py

Task 0

This script takes a URL as a command-line argument,
sends a request to the URL, and displays the body of
the response decoded in UTF-8. If an HTTPError is encountered,
it prints the error code in the format: Error code:
followed by the HTTP status code.

For detailed task description and requirements, refer to the README file.
"""
import urllib.request


if __name__ == "__main__":
    import urllib
    from sys import argv

    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code: ".fromat(e.code))
