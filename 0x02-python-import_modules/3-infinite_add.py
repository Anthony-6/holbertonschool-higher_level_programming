#!/usr/bin/python3
from sys import argv
if len(argv) == 1:
    print('0')
if len(argv) > 1:
    addNumber = 0
    for number in range(1, len(argv)):
        addNumber = (addNumber + int(argv[number]))
    print('{}'.format(addNumber))
if __name__ == "__main__":
    argv
