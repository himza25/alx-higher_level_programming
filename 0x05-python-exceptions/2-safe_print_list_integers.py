#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    printed = 0
    while counter < x:
        try:
            print("{:d}".format(my_list[counter]), end="")
            printed += 1
        except (ValueError, TypeError, IndexError):
            pass
        finally:
            counter += 1
    print("")
    return printed
