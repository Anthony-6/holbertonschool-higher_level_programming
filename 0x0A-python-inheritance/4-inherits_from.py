#!/usr/bin/python3
'''
function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ; otherwise False.
'''


def inherits_from(obj, a_class):
    '''
    this function check if an object is inherited from a specified class
    '''
    if type(obj) != a_class:
        if isinstance(type(obj), a_class):
            return True
        else:
            return False
