#!/usr/bin/python3
def multiple_returns(sentence):
    sen_len = len(sentence)
    if len(sentence) <= 0:
        return sen_len, None
    else:
        first_let = sentence[0]
    return sen_len, first_let
