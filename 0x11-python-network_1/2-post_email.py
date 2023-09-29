#!/usr/bin/python3
"""
A script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib import parse
    from sys import argv

    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode("ascii")
    with urlopen(argv[1], data) as response:
        content = response.read().decode("utf8")
        print(content)
