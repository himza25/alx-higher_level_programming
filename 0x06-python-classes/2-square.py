#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute `size`.
It illustrates control over attribute management with validations.
"""


class Square:
    """
    This class represents a square with validations.

    Attributes:
        __size (int): The size of the square, it must be an integer and >= 0.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int, optional): The size of the new square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
