#!/usr/bin/python3
"""This module defines the MagicClass class to compute the area and
circumference of a circle.
"""

import math


class MagicClass:
    """This class provides methods to compute the area and
    circumference of a circle given its radius.
    """

    def __init__(self, radius=0):
        """Initialize the MagicClass instance.

        Args:
            radius (int, float): The radius of the circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.__radius
