#!/usr/bin/python3
'''
function that returns True if the object is exactly an
instance of the specified class ; otherwise False
'''


def is_same_class(obj, a_class):
    '''
    this function check if an object correspond to a class
    '''
    if type(obj) == a_class:
        return True
