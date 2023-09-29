#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL
and displays the value of a variable in the response header
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    response = requests.get(argv[1])
    header = response.headers.get("X-Request-Id")
    print(header)
