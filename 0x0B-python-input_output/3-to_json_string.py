#!/usr/bin/python3
'''
function that returns the JSON representation
of an object (string)
'''
import json


def to_json_string(my_obj):
    '''
    this function take the my_obj as input and return
    it's JSON representation
    '''
    return json.dumps(my_obj)
