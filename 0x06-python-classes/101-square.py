#!/usr/bin/python3
"""Module with a Square class."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization method with optional size and position."""
        self.size = size
        self.position = position

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
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(coord, int) for coord in value) \
                or any(coord < 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character # and position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Print the square with the character # and position."""
        result = ""
        if self.__size == 0:
            result += "\n"
        else:
            for _ in range(self.__position[1]):
                result += "\n"

            for _ in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size + "\n"

        return result[:-1]
