#!/usr/bin/python3
"""
8-json_api.py

Task 0

This script takes a letter as a command-line argument and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter. The letter
must be sent in the variable q. If no argument is given, q is set to an empty
string.

The script handles the response as follows:
- If the response body is valid JSON and not empty, display the id and name
  in the format: [<id>] <name>.
- If the JSON is invalid, display: Not a valid JSON.
- If the JSON is empty, display: No result.

For detailed task description and requirements, refer to the README file.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    if (len(argv) <= 1):
        values = {"q": ""} 
    else:
        values = {"q": argv[1]}
    response = requests.post(url, data=values)
    try:
        res_json = response.json()
        if (len(res_json) == 0):
            print("No result")
        else:
            res_id = res_json.get('id')
            res_name = res_json.get('name')
            print("[{}] {}".format(res_id, res_name))
    except ValueError as e:
        print("Not a valid JSON")

