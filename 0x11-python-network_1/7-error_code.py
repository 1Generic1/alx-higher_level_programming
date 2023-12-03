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
        if response.status_code >= 400:
            print("Error code:", e.response.status_code)
        else:
            print(response.text)
#    except requests.exceptions.HTTPError as e:
 #       print("Error code:", e)
