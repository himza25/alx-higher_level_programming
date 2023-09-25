#!/usr/bin/python3
from sys import stderr, exc_info as error

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(error()[1]), file=stderr)
        return None
