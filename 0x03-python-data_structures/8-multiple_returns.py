#!/usr/bin/python3
def multiple_returns(sentence):
    sen_len = len(sentence)
    first_let = sentence[0]
    if sen_len == 0:
        return None
    else:
        return sen_len, first_let
