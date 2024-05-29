#!/usr/bin/python3
"""This module defines a Rectangle class."""


class Rectangle:
    """Represents a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle stance.
        Args:
            width: The width of the rectangle
            height: The height of the rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the current width of the rectangle.
        Args:
            value (int): new width of the rectangle
        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the current height of the rectangle.
        Args:
            value (int): new height of the rectangle
        Raises:
            TypeError: if heigh is not an integer.
            ValueError: if heigh is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
