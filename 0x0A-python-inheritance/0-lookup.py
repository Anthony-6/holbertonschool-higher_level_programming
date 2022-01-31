#!/usr/bin/python3
'''
function that return the list of available attributes and methods of an object
'''


def lookup(obj):
    object_ = dir(obj)
    return object_
