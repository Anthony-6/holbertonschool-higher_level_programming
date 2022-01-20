#!/usr/bin/python3
'''Write a class Square that defines a square by: (based on 0-square.py)
    -Private instance attribute: size
    -Instantiation with size (no type/value verification)'''


class Square:
    '''this class declare a square'''
    '''The __init__ method is run as soon as an object of a class is instantiated.
       The method is useful to do any initialization you want to do with your object.
       Notice the double underscores both at the beginning and at the end of the name.'''

    '''Attribute: "__size" create a private instance that is the size of the square'''
    def __init__(self, size):
        self.__size = size
