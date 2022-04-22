#!/usr/bin/python3
''' script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter '''
if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) == 1:
        data = {'q': ''}
    else:
        data = {'q': argv[1]}
    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, data)
    try:
        json = req.json()
        if json == {}:
            print("No result")
        else:
            print("[{}] {}".format(json.get('id'), json.get('name')))
    except Exception:
        print("Not a valid JSON")
