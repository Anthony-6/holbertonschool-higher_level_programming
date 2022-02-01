#!/usr/bin/python3
'''
function that writes an Object to a text file
using a JSON representation

-Prototype: def save_to_json_file(my_obj, filename):
-You must use the with statement
-You don’t need to manage exceptions if the
 object can’t be serialized.
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    this function print object file in json file
    '''
    with open(filename, mode='w', encoding='UTF-8') as myFile:
        return myFile.write(json.dumps(my_obj))
