#!/usr/bin/python3
"""
Sends a POST request with an email and displays the response body.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    response = requests.post(url, data=email)
    print(response.text)
