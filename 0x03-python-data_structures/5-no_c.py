#!/usr/bin/python3
def no_c(my_string):
    c = ''
    for i in my_string:
        if i == 'c' or i == 'C':
            i = ''
        c = c + i
    return c
