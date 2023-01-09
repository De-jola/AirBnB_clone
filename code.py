#!/usr/bin/python3
"""A beautiful code that passes all pycodestyle checks"""


def add(a, b):
    """A function that adds two integers"""
    if type(a) == int and type(b) != int:
        raise TypeError("b must be a whole number")
    elif type(a) != int and type(b) == int:
        raise TypeError("a must be a whole number")
    else:
        return a + b
