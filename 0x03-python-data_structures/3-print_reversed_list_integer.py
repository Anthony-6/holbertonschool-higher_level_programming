#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == 0:
        return None
    for i in list(reversed(my_list)):
        print('{:d}'.format(i))
