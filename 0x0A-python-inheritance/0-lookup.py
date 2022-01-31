#!/usr/bin/python3
'''
function that return the list of available attributes and methods of an object
'''


def lookup(obj):
    '''
    this function return the list of available attributes and method
    of an object
    '''
    return dir(obj)
