#!/usr/bin/python3
"""Module with a MagicClass class."""
import math

class MagicClass:
    """A class that does the same as the given Python bytecode."""

    def __init__(self, radius=0):
        """Initialization method with radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the MagicClass."""
        return 2 * math.pi * self.__radius

    @property
    def radius(self):
        """Retrieve the value of the radius attribute."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Set the value of the radius attribute."""
        if type(value) is not int and type(value) is not float:
            raise TypeError("radius must be a number")
        self.__radius = value
