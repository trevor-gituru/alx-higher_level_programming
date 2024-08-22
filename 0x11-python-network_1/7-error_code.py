#!/usr/bin/python3
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
