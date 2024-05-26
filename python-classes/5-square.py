#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square instance.
        Args:
            size: The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Getter for the current size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the current size of the Square.
        Raises:
            TypeError: if size is not an int.
            ValueError: if size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

            Returns:
                int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the Square with the character '#'/"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
