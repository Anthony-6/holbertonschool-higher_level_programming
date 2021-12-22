#!/usr/bin/python3
def uppercase(str):
    string = ""
    for let in str:
        if (ord(let) >= 97 and ord(let) <= 122):
            string = (string + chr(ord(let) - 32))
        else:
            string = (string + chr(ord(let)))
    print('{}'.format(string))
