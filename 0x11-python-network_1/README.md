# 0x11. Python - Network #1
This directory contains python scripts that use urllib and requests modules to do the following:
- [0-hbtn_status.py](0-hbtn_status.py) - fetches `https://alx-intranet.hbtn.io/status`
- [1-hbtn_header.py](1-hbtn_header.py) - takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response
- [2-post_email.py](2-post_email.py) - takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)