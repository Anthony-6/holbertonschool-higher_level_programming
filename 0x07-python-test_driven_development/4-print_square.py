#!/usr/bin/python3
'''
    -Prototype: def print_square(size):
    -size is the size length of the square
    -size must be an integer, otherwise raise
    a TypeError exception with the message size must be an integer
    -if size is less than 0, raise a ValueError exception with the
    message size must be >= 0
'''


def print_square(size):
    '''
    This function print a square with parameter size
    '''
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for i in range(size):
            for j in range(size):
                print('#', end='')
            print('')
