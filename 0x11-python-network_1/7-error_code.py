#!/usr/bin/python3
"""
Script to send a GET request to a URL and display the body of the response.
If the HTTP status code is greater than or equal to 400, print an error message.
"""

import requests
import sys

if __name__ == "__main__":
    url =sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
        if response.status_code >= 400:
            print("Error code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

