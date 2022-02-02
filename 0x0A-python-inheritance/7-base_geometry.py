#!/usr/bin/python3
'''
class BaseGeometry (based on 5-base_geometry.py).

-Public instance method: def area(self): that raises an
 Exception with the message area() is not implemented
-Public instance method: def integer_validator(self, name, value):
 that validates value:
    -you can assume name is always a string
    -if value is not an integer: raise a TypeError exception,
    with the message <name> must be an integer
    -if value is less or equal to 0: raise a ValueError exception
    with the message <name> must be greater than 0
'''


class BaseGeometry:
    '''
    this class define a function base geometry
    '''
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('<name> must be an integer')
        if value <= 0:
            raise ValueError('<name> must be greater than 0')
