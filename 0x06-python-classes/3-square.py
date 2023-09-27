#!/usr/bin/python3
"""
This module defines a Square class that calculates the area of a square.
It inherits from the square class with size validations.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square, it must be an integer and >= 0.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int, optional): The size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
