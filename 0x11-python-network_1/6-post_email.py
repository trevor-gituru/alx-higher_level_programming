#!/usr/bin/python3
"""
6-post_email.py

Task 0

This script takes a URL and an email address, sends a POST request to the
URL with the email as a parameter, and displays the body of the response.

For detailed task description and requirements, refer to the README file.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    email = argv[2]
    url = argv[1]
    values = {"email": email}
    response = requests.post(url, data=values)
    content = respone.text
    print(content)
