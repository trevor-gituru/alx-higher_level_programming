#!/usr/bin/python3
"""
4-hbtn_status.py

Task 0

This script fetches https://alx-intranet.hbtn.io/status using the requests
package and displays the body of the response in a specific format.

For detailed task description and requirements, refer to the README file.
"""

if __name__ == "__main__":
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    content = response.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
