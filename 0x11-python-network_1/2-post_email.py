#!/usr/bin/python3
"""
2-post_email.py

Task 0

This script takes a URL and an email address as command-line arguments,
sends a POST request to the URL with the email address as a parameter,
and displays the body of the response decoded in UTF-8.

For detailed task description and requirements, refer to the README file.
"""
import urllib.parse
import urllib.request


if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from sys import argv

    email = argv[2]
    url = argv[1]
    values = {"email": email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    request = Request(url, data)

    with urlopen(request) as respone:
        content = respone.read()
        content = content.decode('utf8')
        print(content)
