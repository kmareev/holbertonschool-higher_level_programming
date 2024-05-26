#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size: The size of the square.

        Raises:
            TypeError: if size is not an int.
            ValueError: if size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculates the area of the square.

            Returns:
                int: The area of the square.
        """
        return self.__size ** 2
