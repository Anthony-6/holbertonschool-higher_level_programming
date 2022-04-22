#!/usr/bin/python3
''' script that takes in a URL, sends a request to the URL and
    displays the body of the response '''
if __name__ == "__main__":
    import requests
    import sys

    req = requests.get(sys.argv[1])
    if req.status_code > 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
