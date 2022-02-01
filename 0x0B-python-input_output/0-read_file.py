#!/usr/bin/python3
'''
function that reads a text file (UTF8) and prints it to stdout:

Prototype: def read_file(filename=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
'''


def read_file(filename=""):
    '''
    this function open a file called my_file_0.txt and read it
    '''
    with open(filename, encoding='UTF-8') as myFile:
        print(myFile.read(), end='')
