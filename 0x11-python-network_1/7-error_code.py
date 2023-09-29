#!/usr/bin/python3
"""
A script that takes in a URL,
sends a request to the URL
and displays the body of the response
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error code: {response.status_code}")
