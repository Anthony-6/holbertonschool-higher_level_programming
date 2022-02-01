#!/usr/bin/python3
'''
function that creates an Object from a “JSON file”:

-Prototype: def load_from_json_file(filename):
-You must use the with statement
-You don’t need to manage exceptions if the JSON string
 doesn’t represent an object.
-You don’t need to manage file permissions / exceptions.
'''
import json


def load_from_json_file(filename):
    '''
    this function read the content of a given file and transform
    it into a json file
    '''
    with open(filename, mode='r', encoding='utf-8') as myFile:
        content = myFile.read()
        return json.loads(content)
