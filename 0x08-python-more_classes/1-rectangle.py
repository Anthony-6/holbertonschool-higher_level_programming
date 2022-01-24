#!/usr/bin/python3
'''
    Write a class Rectangle that defines a rectangle by:
    (based on 0-rectangle.py)

    -Private instance attribute: width:
        -property def width(self): to retrieve it
        -property setter def width(self, value): to set it:
            -width must be an integer, otherwise raise a TypeError
             exception with the message width must be an integer
            -if width is less than 0, raise a ValueError exception
             with the message width must be >= 0
    -Private instance attribute: height:
        -property def height(self): to retrieve it
        -property setter def height(self, value): to set it:
            -height must be an integer, otherwise raise a TypeError
            exception with the message height must be an integer
            -if height is less than 0, raise a ValueError exception
            with the message height must be >= 0
    -Instantiation with optional width and height:
    def __init__(self, width=0, height=0):
'''


class Rectangle:
    '''this class define a rectangle
        with width and height to define the size of the rectangle
    '''
    valuemess = 'height must be >= 0'
    typemess = 'height must be an integer'
    valuemessW = 'width must be >= 0'
    typemessW = 'width must be an integer'

    def __init__(self, width=0, height=0):

        if type(width) is not int:
            raise TypeError(typemessW)
        elif width < 0:
            raise ValueError(valuemessW)
        if type(height) is not int:
            raise TypeError(typemess)
        elif height < 0:
            raise ValueError(valuemess)
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError(typemess)
        elif value < 0:
            raise ValueError(valuemess)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError(typemess)
        elif value < 0:
            raise ValueError(valuemess)
        self.__height = value
