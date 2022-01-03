#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temp = my_list
    temp[idx] = element
    if idx >= 0 and idx < len(temp):
        return temp
    else:
        return None
    if idx < 0:
        return temp
    else:
        return None
