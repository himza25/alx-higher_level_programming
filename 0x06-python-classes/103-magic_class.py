#!/usr/bin/python3
import math

"""
This module defines the MagicClass.
It provides a way to calculate the area and circumference of a circle.
"""


class MagicClass:
    """
    This class represents a circle.
    It allows setting and getting the radius of the circle,
    calculating the area, and calculating the circumference.
    """

    def __init__(self, radius=0):
        """Initialize a new MagicClass with radius."""
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
