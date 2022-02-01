#!/usr/bin/python3
'''
function that appends a string at the end of a
text file (UTF8) and returns the number of characters added:

Prototype: def append_write(filename="", text=""):
If the file doesn’t exist, it should be created
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
'''


def append_write(filename="", text=""):
    '''
    this function add a text a the end of a file and return
    the number of character
    '''
    with open(filename, mode='a', encoding='UTF-8') as myFile:
        return myFile.write(text)
