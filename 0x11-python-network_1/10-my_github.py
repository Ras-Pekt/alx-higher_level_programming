#!/usr/bin/python3
"""
takes GitHub credentials
and uses the GitHub API to display user id
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    user = argv[1]
    token = argv[2]

    url = f"https://api.github.com/users/{user}"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    id = response.json().get("id")
    print(id)
