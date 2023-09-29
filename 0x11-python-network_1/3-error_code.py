#!/usr/bin/python3
"""
A script that takes in a URL,
sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from sys import argv

    try:
        with urlopen(argv[1]) as response:
            content = response.read().decode("utf8")
            print(content)
    except HTTPError as e:
        print(f"Error code: {e.code}")
