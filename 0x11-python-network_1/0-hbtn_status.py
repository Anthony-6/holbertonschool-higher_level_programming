#!/usr/bin/python3
''' script that fetches https://intranet.hbtn.io/status and display
    information about the url '''
if __name__ == "__main__":

    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as myUrl:
        body = myUrl.read()
        bodyutf = body.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(body.__class__))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(bodyutf))
