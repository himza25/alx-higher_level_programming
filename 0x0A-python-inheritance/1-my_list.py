#!/usr/bin/python3

"""
This module contains a class MyList that inherits from list.
The class has a public instance method to print the list in sorted order.
"""


class MyList(list):
    """
    MyList class that inherits from list.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
