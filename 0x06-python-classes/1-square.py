#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute `size`.
It illustrates control over attribute management using private variables.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
