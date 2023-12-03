#!/usr/bin/python3
"""
Script to send a POST request to a URL with an email parameter and display the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
