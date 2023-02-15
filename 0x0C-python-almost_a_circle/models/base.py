#!/usr/bin/python3
# base.py
"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """
    A base class to manage id attribute in all future classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor method for the Base class

        Args:
            id (int): The id of the instance (optional)

        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
