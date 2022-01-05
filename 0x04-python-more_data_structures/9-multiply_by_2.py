#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    second_dict = {}
    for i in a_dictionary:
        second_dict[i] = a_dictionary[i] * 2
    return second_dict
            