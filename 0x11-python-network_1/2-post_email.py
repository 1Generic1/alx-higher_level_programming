#!/usr/bin/python3
"""
Script to send a POST request with an email parameter to a URL and display the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    email = sys.argv[2]
    data = {'email': email}
    data = urllib.parse.urlencode(data).encode('utf-8')
    
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url, data) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.URLError as e:
        print("Error: {}".format(e))
        sys.exit(1)
