#!/usr/bin/python3

"""
This module contains a class named BaseGeometry with a method that raises
an exception.
"""


class BaseGeometry:
    """
    A class that serves as the base for other geometry-related classes.
    Includes a method for calculating area, which is not yet implemented.
    """

    def area(self):
        """
        Raises an exception to indicate that the method is not implemented.
        """
        raise Exception("area() is not implemented")
