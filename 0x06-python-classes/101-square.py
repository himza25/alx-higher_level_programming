#!/usr/bin/python3

"""
This module defines a Square class
It provides a way to create Square objects with optional
size and position, get area, and print the Square
"""


class Square:
    """
    This class represents a Square.
    It allows setting and getting the size and position of the Square,
    calculating the area, and printing the Square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the Square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the Square."""
        if type(value) is not tuple or \
           len(value) != 2 or \
           type(value[0]) is not int or \
           type(value[1]) is not int or \
           value[0] < 0 or \
           value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the Square."""
        return self.__size ** 2

    def my_print(self):
        """Print the Square using the '#' character."""
        if self.__size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Provide the string representation of the Square,
        same as my_print."""
        output = []
        if self.__size == 0:
            return ""
        for i in range(self.__position[1]):
            output.append("")
        for i in range(self.__size):
            output.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(output)
