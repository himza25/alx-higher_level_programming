#!/usr/bin/python3
"""Defines a class LockedClass with restricted attribute assignment."""


class LockedClass:
    """Prevents dynamic attribute creation except for 'first_name'."""
    __slots__ = ['first_name']
