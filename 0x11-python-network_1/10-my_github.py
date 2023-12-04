#!/usr/bin/python3
"""
Script to display your GitHub id using the GitHub API and Basic Authentication.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    personal_access_token = sys.argv[2]
    try:
        url = "https://api.github.com/user"
        response = requests.get(url, auth=(username, personal_access_token))
        user_data = response.json()
        github_id = user_data.get('id')
        if github_id:
            print(github_id)
        else:
            print("None")
    except Exception as e:
        print("Error:", e)
