#!/usr/bin/python3
'''
-class Rectangle that inherits from BaseGeometry
 (7-base_geometry.py). (task based on 8-rectangle.py)

-Instantiation with width and height: def __init__(self, width, height)::
    -width and height must be private. No getter or setter
    -width and height must be positive integers validated by integer_validator
-the area() method must be implemented
-print() should print, and str() should return, the following
 rectangle description:
-[Rectangle] <width>/<height>
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    this class create a rectangle based on BaseGeometry and take
    two argument as value
    '''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)

    def area(self):
        print('[Rectangle] {:d}/{:d}'.format(self.__width, self.__height))
        return self.__width * self.__height
