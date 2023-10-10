#!/usr/bin/python3
"""This module contains a class MyList that inherits from list."""

class MyList(list):
    """MyList class that inherits from list.
    
    Public instance method:
        def print_sorted(self): prints the list, but sorted (ascending sort)
    """
    
    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
