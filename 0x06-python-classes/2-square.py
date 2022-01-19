#!/usr/bin/python3
'''Write a class Square that defines a square by: (based on 1-square.py)

    -Private instance attribute: size
    -Instantiation with optional size: def __init__(self, size=0):
    -size must be an integer, otherwise raise a TypeError exception
     with the message size must be an integer'''
valuemes = "size must be >= 0"
typemess = "size must be an integer"


class Square:
    '''this class defines a square'''
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError(typemess)
        elif size < 0:
            raise ValueError(valuemes)
