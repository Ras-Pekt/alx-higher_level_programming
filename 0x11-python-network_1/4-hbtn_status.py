#!/usr/bin/python3
"""
A fetches https://alx-intranet.hbtn.io/status using the package requests
"""

if __name__ == "__main__":
    import requests

    response = requests.get("https://alx-intranet.hbtn.io/status")
    print(f"Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
