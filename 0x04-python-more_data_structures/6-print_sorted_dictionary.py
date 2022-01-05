#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = dict(sorted(a_dictionary.items(), key=lambda x: x[0]))
    for i, j in sorted_dic.items():
        print('{}: {}'.format(i, j))
