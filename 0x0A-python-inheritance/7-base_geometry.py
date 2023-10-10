#!/usr/bin/python3

"""
This module contains a class named BaseGeometry with methods that raise
exceptions.
"""


class BaseGeometry:
    """
    A class that serves as the base for other geometry-related classes.
    Includes methods for calculating area and validating integer values.
    """

    def area(self):
        """
        Raises an exception to indicate that the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer.

        Parameters:
            name (str): The name of the value, assumed to always be a string.
            value (int): The value to validate.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
