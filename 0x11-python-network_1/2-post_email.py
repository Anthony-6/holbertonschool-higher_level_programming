#!/usr/bin/python3
''' Python script that takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable found in
    the header of the response '''
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    myRequest = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(myRequest) as myResponse:
        response = myResponse.read()
        response = response.decode('utf-8')
        print(response)
