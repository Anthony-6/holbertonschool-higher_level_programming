#!/usr/bin/python3
for i in range (99):
    print('{:02d}'.format(i), end = ", ")
    if i == 98:
        print('{:d}\n'.format(i+1))
    