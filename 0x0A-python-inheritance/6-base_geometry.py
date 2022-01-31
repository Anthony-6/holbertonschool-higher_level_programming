#!/usr/bin/python3
'''
class BaseGeometry (based on 5-base_geometry.py).

Public instance method: def area(self): that raises an
Exception with the message area() is not implemented
'''


class BaseGeometry:
    '''
    this class define a function base geometry
    '''
    def area(self):
        raise Exception('area() is not implemented')
