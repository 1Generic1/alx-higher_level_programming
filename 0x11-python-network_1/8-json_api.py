#!/usr/bin/python3
"""
Script to send a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter.
"""

import requests
import sys


if __name__ == "__main__":
    q = "" if len(sys.argv) < 2 else sys.argv[1]
    try:
        response = requests.post(
            "http://0.0.0.0:5000/search_user",
            data={'q': q}
        )
        json_response = (
            response.json() if response.headers.get('content-type')
            == 'application/json'
            else None
        )
        if json_response == {}:
            print("No result")
        if (
            json_response and isinstance(json_response, dict) and
            json_response.get('id') and json_response.get('name')
        ):
            print("[{}] {}".format(json_response['id'], json_response['name']))
    except ValueError:
        print("Not a valid JSON")
