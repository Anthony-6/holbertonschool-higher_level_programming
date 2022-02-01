#!/usr/bin/python3
'''
function that returns an object (Python data structure)
represented by a JSON string
'''
import json


def from_json_string(my_str):
    '''
    this function take my_str as input and return an object
    in JSON string representation
    '''
    return json.loads(my_str)
