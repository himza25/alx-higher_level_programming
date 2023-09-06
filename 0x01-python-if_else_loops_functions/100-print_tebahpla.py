#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        print("{}".format(chr(i - 1).upper()), end="")
    print("{}".format(chr(i)), end="")
