#!/usr/bin/python3

from models.base import Base
import os



class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):

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
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
    
    def area(self):
        return self.__width * self.__height

    def display(self):
        for posY in range(self.__y):
            print()
        for recHeight in range(self.__height):
            for posX in range(self.__x):
                print(' ', end='')
            for recWidth in range(self.__width):
                print('#', end='')
            print()
    
    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        if len(args) > 1:
            myArg = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, myArg[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
