#!/usr/bin/python3
'''
-class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

-Instantiation with width and height: def __init__(self, width, height):
-width and height must be private. No getter or setter
-width and height must be positive integers, validated by integer_validator
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    this class create a rectangle based that inherat from base_geometry
    and take width and height as value
    '''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)
