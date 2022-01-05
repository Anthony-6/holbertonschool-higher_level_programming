#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    max_dic = max(a_dictionary, key=lambda x: a_dictionary[x])
    return max_dic
