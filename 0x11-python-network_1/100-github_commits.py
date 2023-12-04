#!/usr/bin/python3
"""
Script to list 10 commits (from the most recent to oldest) of a repository
by a specific user using the GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    try:
        url = (
            f"https://api.github.com/repos"
            f"/{owner_name}/{repository_name}/commits"
        )
        params = {"per_page": 10}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            commits = response.json()
            for commit in reversed(commits):
                sha = commit["sha"]
                author_name = commit["commit"]["author"]["name"]
                print("{}: {}".format(sha, author_name))
        else:
            print("Error: {}".format(response.status_code))
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
