#!/usr/bin/python3
"""
This module contains a class MyList that inherits from the built-in list class.
The class has a public instance method called print_sorted,
which prints the list in ascending order.
"""


class MyList(list):
    """
    MyList class that inherits from the built-in list class.
    """
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
