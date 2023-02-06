#!/usr/bin/python3
"""function that returns the list of available attributes and methods of an object"""

def lookup(obj):
    """Returns list of attributes and methods
    Args:
         -obj: object to look into
    """

    return dir(obj)
