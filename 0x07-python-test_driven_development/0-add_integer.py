#!/usr/bin/python3
"""This module contains a function that adds two integers."""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float (default is 98).

    Returns:
        The sum of a and b as an integer.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
