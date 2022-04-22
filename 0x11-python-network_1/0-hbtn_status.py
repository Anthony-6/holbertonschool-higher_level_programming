#!/usr/bin/python3
''' script that fetches https://intranet.hbtn.io/status and display
    information about the url '''

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as myUrl:
    body = myUrl.read()
    bodyutf = body.decode('utf-8')
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(body.__class__, body, bodyutf))
