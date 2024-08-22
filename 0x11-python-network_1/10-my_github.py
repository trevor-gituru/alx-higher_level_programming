#!/usr/bin/python3
"""
10-my_github.py

Task 0

This script takes your GitHub credentials (username and password) and uses the
GitHub API to display your user ID. Basic Authentication is used with a
personal access token as the password.

For detailed task description and requirements, refer to the README file.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = ''
    user = argv[1]
    token = argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(user, token))
    user_id = response.json().get('id')
    print(user_id)
