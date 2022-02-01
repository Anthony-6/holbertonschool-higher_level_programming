#!/usr/bin/python3
'''
function that writes a string to a text file (UTF8) and
returns the number of characters written:

Prototype: def write_file(filename="", text=""):
You must use the with statement
You don’t need to manage file permission exceptions.
Your function should create the file if doesn’t exist.
Your function should overwrite the content of the file if it already exists.
'''


def write_file(filename="", text=""):
    '''
    this function write text on a file and return the number of character
    '''
    with open(filename, mode='w', encoding='UTF-8') as myFile:
        return myFile.write(text)
