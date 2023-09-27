#!/usr/bin/python3
"""
This module defines a Square class that calculates the area of a square.
It has a getter and setter method for the size property.
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
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
