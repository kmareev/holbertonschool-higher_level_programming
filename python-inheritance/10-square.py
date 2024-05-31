#!/usr/bin/python3
"""This is a Square class that inherits from
Rectangle base class."""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A subclass of Rectangle representing
    a Square."""

    def __init__(self, size):
        """Initialize a square with a given size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    
    def area(self):
        """Calculates the area of a Square.
        Returns:
            int area of the square."""
        return self.__size * self.__size
    
    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"