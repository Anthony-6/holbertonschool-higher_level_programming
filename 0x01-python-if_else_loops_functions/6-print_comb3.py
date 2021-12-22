#!/usr/bin/python3
for u in range(0, 10):
    for d in range(1, 10):
        if u < d:
            print("{}".format(u), end="")
            if u < 8:
                print("{}".format(d), end=", ")
            else:
                print("{}".format(d))
