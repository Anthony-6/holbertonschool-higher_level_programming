#!/usr/bin/python3
from sys import argv
if len(argv) == 1:
    print('0 arguments.')
else:
    if len(argv) == 2:
        print('1 argument:')
    if len(argv) > 2:
        print(len(argv)-1, 'arguments: ')
    for arg in range(1, len(argv)):
        print(arg, ': ', argv[arg], sep="")
if __name__ == "__main__":
    len(argv)
