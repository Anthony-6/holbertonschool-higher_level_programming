#!/usr/bin/python3
from sys import argv
if len(argv) == 1:
    print('0 arguments.')
else:
    if len(argv) == 2:
        print('1 argument:')
    elif len(argv) > 2:
        print('arguments: {}'.format(len(argv)-1))
    for arg in range(1, len(argv)):
        print('{}: {:s}'.format(arg, argv[arg]))
if __name__ == "__main__":
    len(argv)
