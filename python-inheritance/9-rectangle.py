#!/usr/bin/python3
"""This is base class for geometry operation.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a Rectangle."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of a rectangle.
        Returns:
            int area of a rectangle."""
        return self.__width * self.__height
    
    def __str__(self):
        """Return the string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
