#!/usr/bin/python3
'''
function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ; otherwise False.
'''


def inherits_from(obj, a_class):
    '''
    this function check if an object is inherited from a specified class
    '''
    return type(obj) != a_class:
