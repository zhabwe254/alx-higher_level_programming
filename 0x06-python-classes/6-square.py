#!/usr/bin/python3
"""Module with a Square class."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization method with optional size and position."""
        self.__size = size
        self.__position = position

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(isinstance(i, int) for i in position) or any(i < 0 for i in position):
            raise ValueError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """Retrieve the value of the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the value of the position attribute."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
            raise ValueError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """
