#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    repo_name = argv[1]
    owner_name = argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    response = requests.get(url)
    count = 0

    for item in response.json():
        if count == 10:
            break

        sha = item.get("sha")
        commit_author = item.get("commit").get("author").get("name")

        print(f"{sha}: {commit_author}")
        count += 1
