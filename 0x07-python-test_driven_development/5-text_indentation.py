#!/usr/bin/python3
"""This module contains a function that indents text."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text: The text to be indented.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    for char in text:
        new_text += char
        if char in ".?:":
            new_text += "\n\n"

    print(new_text.strip())
