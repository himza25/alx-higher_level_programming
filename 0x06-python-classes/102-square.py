#!/usr/bin/python3

"""
This module defines a Square class.
It provides a way to create Square objects with a size,
get area, and perform comparisons based on area.
"""


class Square:
    """
    This class represents a Square.
    It allows setting and getting the size of the Square,
    calculating the area, and performing comparisons based on area.
    """

    def __init__(self, size=0):
        """Initialize a new Square."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the Square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if this square is less than another square based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square is less than or equal to another square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if this square is greater than another square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square is greater than or equal to another square."""
        return self.area() >= other.area()
