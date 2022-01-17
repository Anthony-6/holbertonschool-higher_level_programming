#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        print("".join(map(str, my_list[:x])))
        for elem in my_list[:x]:
            count += 1
        return count
        safe_print_list(x)
    except TypeError:
        count = 0
        print("".join(map(str, my_list[:x])))
        for elem in my_list[:x]:
            count += 1
        return count
        safe_print_list(x)
