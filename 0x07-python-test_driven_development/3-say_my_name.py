#!/usr/bin/python3
"""This module contains a function that prints a full name."""


def say_my_name(first_name, last_name=""):
    """
    Prints a full name.

    Args:
        first_name: The first name as a string.
        last_name: The last name as a string (default is an empty string).

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
