#!/usr/bin/python3
"""Module with a Square class."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initialization method with optional size."""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """Retrieve the value of the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
