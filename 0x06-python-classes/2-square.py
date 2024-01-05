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
