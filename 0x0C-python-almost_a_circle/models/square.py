#!/usr/bin/python3
'''
this function create a square that inherats from the rectangle
by importating Rectangle class
'''
from models.rectangle import Rectangle
'''
class Square that inherits from Rectangle:

In the file models/square.py
Class Square inherits from Rectangle
Class constructor: def __init__(self, size, x=0, y=0, id=None)::
Call the super class with id, x, y, width and height - this super call will
use the logic of the __init__ of the Rectangle class. The width and height
must be assigned
to the value of size
You must not create new attributes for this class, use all attributes of
Rectangle -
As reminder: a Square is a Rectangle with the same width and height
All width, height, x and y validation must inherit from Rectangle - same
behavior in case
of wrong data
The overloading __str__ method should return [Square] (<id>) <x>/<y> - <size> -
in our case,
width or height
'''


class Square(Rectangle):
    '''
    this class define a square based on the rectangle file
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        initialize value and set them to 0
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
        this function return the attributs of the square in string format
        '''
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        '''
        define the size of the square based on the width value
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        define val as value for the square, it set the value of
        size by using width and height value
        '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
        check if there is more than 1 and 5 arg in our list
        break the loop if there is more than five arg
        '''
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            myArg = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if i != 5:
                    setattr(self, myArg[i], args[i])

    def to_dictionary(self):
        '''
        this function return the dictionnary of square
        '''
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
