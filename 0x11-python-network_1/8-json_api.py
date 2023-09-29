#!/usr/bin/python3
"""
A script that takes in a letter
and sends a POST request
with the letter as a parameter
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]

    url = "http://0.0.0.0:5000/search_user"
    values = {"q": q}

    response = requests.post(url, data=values)

    try:
        if len(response.json()) == 0:
            print("No result")
        else:
            id = response.json().get("id")
            name = response.json().get("name")
            print(f"[{id}] {name}")
    except Exception:
        print("Not a valid JSON")
