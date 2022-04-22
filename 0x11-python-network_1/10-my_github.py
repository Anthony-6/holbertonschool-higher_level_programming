#!/usr/bin/python3
''' script that takes your GitHub credentials (username and password) and
    uses the GitHub API to display your id '''
if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    pwd = sys.argv[2]
    url = "https://api.github.com/user"

    userdat = requests.get(url, auth=(username, pwd))
    userjson = userdat.json()
    print(userjson.get('id'))
