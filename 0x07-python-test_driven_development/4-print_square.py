#!/usr/bin/python3
"""This module contains a function that prints a square."""


def print_square(size):
    """
    Prints a square using the character #.

    Args:
        size: The size length of the square.

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
