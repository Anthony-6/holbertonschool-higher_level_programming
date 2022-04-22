#!/usr/bin/python3
''' script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8). '''
if __name__ == "__main__":
    import urllib.request
    import sys
    url = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(url) as myUrl:
            body = myUrl.read()
            body = body.decode('utf-8')
            print(body)
    except urllib.error.URLError as error:
        print("Error code: {}".format(error.code))
