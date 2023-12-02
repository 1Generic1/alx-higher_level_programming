#!/usr/bin/python3
""" this script displays the value of the X-Request-Id"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            if 'X-Request-Id' in response.headers:
                x_request_id = response.headers['X-Request-Id']
                print(x_request_id)
            else:
                print("X-Request-Id not found in the response header.")
    except urllib.error.URLError as e:
        print("Error: {}".format(e))
        sys.exit(1)
