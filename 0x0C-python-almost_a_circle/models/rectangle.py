#!/usr/bin/python3
'''
this program create a rectangle with information imported by Base
file
'''
from models.base import Base
'''
class Rectangle that inherits from Base:

In the file models/rectangle.py
Class Rectangle inherits from Base
Private instance attributes, each with its own public getter and setter:
__width -> width
__height -> height
__x -> x
__y -> y
Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
Call the super class with id - this super call with use the logic of the
__init__ of
the Base class
Assign each argument width, height, x and y to the right attribute
'''


class Rectangle(Base):
    '''
    class rectangle that inherit from base class
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        this function create value for rectangle and check if value are
        correct and raise error if not
        '''
        super().__init__(id)
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''
        set width as private value
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        define value and check if it's value is correct and raise error if not
        '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''
        set height as private value
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        define value and check if it's value is correct and raise error if not
        '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def x(self):
        '''
        set x as a private value
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        define value and check if it's value is correct and raise error if not
        '''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''
        set y as a private value
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        define value and check if it's value is correct and raise error if not
        '''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''
        return the area of the rectangle
        '''
        return self.__width * self.__height

    def display(self):
        '''
        display the rectangle in a visual form when executed
        '''
        for posY in range(self.__y):
            print()
        for recHeight in range(self.__height):
            for posX in range(self.__x):
                print(' ', end='')
            for recWidth in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        '''
        return the string format of the information of the rectangle
        '''
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        '''
        check if there is more than 1 and 5 arg in our list
        break the loop if there is more than five arg
        '''
        if len(args) > 1:
            myArg = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                if i > 5:
                    break
                else:
                    setattr(self, myArg[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''
        return the dictionnary of rectangle
        '''
        return self.__dict__
