#!/usr/bin/python3
"""Module for MyInt class"""


class MyInt(int):
    """MyInt is a rebel class that inherits from int.
    It has == and != operators inverted.
    """

    def __eq__(self, other):
        """Override the equality operator to behave like the != operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator to behave like the == operator."""
        return super().__eq__(other)
