#!/usr/bin/python3
'''script that fetches an url using requests package'''
if __name__ == "__main__":
    import requests

    request = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(request.text.__class__))
    print('\t- content: {}'.format(request.text))
