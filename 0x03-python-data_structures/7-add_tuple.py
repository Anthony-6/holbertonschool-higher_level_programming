#!/usr/bin/python3
def check_tuple(tuple_check=()):
    if len(tuple_check) > 2:
        tuple_check = (tuple_check[0], tuple_check[1])
    elif len(tuple_check) <= 1:
        if len(tuple_check) == 1:
            tuple_check = (tuple_check[0], 0)
        if len(tuple_check) == 0:
            tuple_check = (0, 0)
    return tuple_check


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = check_tuple(tuple_a)
    tuple_b = check_tuple(tuple_b)
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
