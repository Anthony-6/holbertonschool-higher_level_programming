#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result_tuple = tuple(map(lambda x, y: x + y, tuple_a, tuple_b))
    for i in tuple(tuple_a):
        if i > 2:
            tuple_a = tuple_a[0:1]
    for i in tuple(tuple_b):
        if i > 2:
            tuple_a = tuple_b[0:1]
    for j in tuple(tuple_a):
        if j < 2:
            j = tuple_a[0:1]
    for j in tuple(tuple_b):
        if j < 2:
            j = tuple_a[0:1]
    return (result_tuple)