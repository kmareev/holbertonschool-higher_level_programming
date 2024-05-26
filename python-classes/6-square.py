#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance.
        Args:
            size: The size of the square.
            position: The position of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for the current position of the Square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the current position of the Square.

        Args:
            value: The new position.
        Raises:
            TypeError: if position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(i, int) for i in value) \
                or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
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
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.size):
                print(" " * self.__position[0], end="")
                print("#" * self.size)
