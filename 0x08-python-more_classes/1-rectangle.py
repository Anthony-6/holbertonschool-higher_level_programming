#!/usr/bin/python3
class Rectangle:
    '''this class define a rectangle
        with width and height to define the size of the rectangle
    '''
    valuemess = 'height must be >= 0'
    typemess = 'height must be an integer'

    def __init__(self, width=0, height=0):

        if type(width) is not int:
            raise TypeError(typemess)
        elif width < 0:
            raise ValueError(valuemess)
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
