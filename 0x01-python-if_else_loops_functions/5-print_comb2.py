#!/usr/bin/python3
for i in range(99):
    print('{:02d}'.format(i), end=", ")
    if i == 98:
        print('{:d}'.format(i+1))
