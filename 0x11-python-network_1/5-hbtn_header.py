#!/usr/bin/python3
"""
Script to send a request to a URL and display the value of the variable "X-Request-Id" in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        if 'X-Request-Id' in response.headers:
            x_request_id = response.headers['X-Request-Id']
            print(x_request_id)
        else:
            print("X-Request-Id not found in the response header.")
    except requests.exceptions.RequestException as e:
            print("Error:", e)
