#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    count = len(args)
    print("{} argument{}{}"
          .format(count, "" if count == 1 else "s", ":" if args else "."))
    for i, arg in enumerate(args):
        print("{}: {}".format(i + 1, arg))
