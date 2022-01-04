#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    List = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            List.append(True)
        else:
            List.append(False)
    return List