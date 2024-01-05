#!/usr/bin/python3
"""Module with a Square class."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initialization method with size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the value of the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of the size attribute."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal based on the area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal based on the area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if the area of the first square is less than the second."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area of the first square is less than or equal to the second."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if the area of the first square is greater than the second."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area of the first square is greater than or equal to the second."""
        return self.area() >= other.area()
