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
    -Public class attribute number_of_instances:
        -Initialized to 0
        -Incremented during each new instance instantiation
        -Decremented during each instance deletion
    -Public class attribute print_symbol:
        -Initialized to #
        -Used as symbol for string representation
        -Can be any type
    -Instantiation with optional width and height:
    def __init__(self, width=0, height=0):
    -Public instance method: def area(self): that returns
    the rectangle area
    -Public instance method: def perimeter(self):
    that returns the rectangle perimeter:
        -if width or height is equal to 0, perimeter is equal to 0
    -print() and str() should print the rectangle with the character
    #: (see example below)
        -if width or height is equal to 0, return an empty string
    -Print the message "Bye rectangle..." (... being 3 dots not ellipsis)
     when an instance of Rectangle is deleted
    -Static method def bigger_or_equal(rect_1, rect_2): that returns the
    biggest rectangle based on the area
        -rect_1 must be an instance of Rectangle, otherwise raise
         a TypeError exception with the message rect_1 must be an
         instance of Rectangle
        -rect_2 must be an instance of Rectangle, otherwise raise
         a TypeError exception with the message rect_2 must be an
         instance of Rectangle
        -Returns rect_1 if both have the same area value
    -Class method def square(cls, size=0): that returns a new Rectangle
     instance with width == height == size
'''


class Rectangle:
    '''this class define a rectangle
        with width and height to define the size of the rectangle
    '''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):

        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
        self.__width = width

        Rectangle.number_of_instances += 1

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
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    print(self.print_symbol, end='')
                if i != self.__height - 1:
                    print()
        return ''

    def __repr__(self):
        return 'Rectangle({}, {})'.format(
            eval(str(self.__width)), eval(str(self.__height)))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        else:
            if rect_1.area() == rect_2.area():
                return rect_1
            elif rect_1.area() > rect_2.area():
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
