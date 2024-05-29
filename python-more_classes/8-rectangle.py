#!/usr/bin/python3
"""This module defines a Rectangle class."""


class Rectangle:
    """Represents a Rectangle."""

    number_of_instances = 0  # Class attribute to keep track of the \
    # number of instances
    print_symbol = '#'  # Class attribute for symbol used in \
    # string representation

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle stance.
        Args:
            width: The width of the rectangle
            height: The height of the rectangle.
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Incrementing number of instances

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

    def area(self):
        """Calculates the area of the rectangle.

            Returns:
                int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

            Returns:
                int: The perimeter of the rectangle, or 0 if either width or
                height is 0.
            """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle using the
        '#' character.

        If either width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for _ in range(self.__height):
            rect_str += str(self.print_symbol) * self.__width + "\n"
        return rect_str.rstrip()

    def __repr__(self):
        """Returns a string representation of the rectangle that
        can recreate a new instance using eval."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the bigger area.
        
        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.
        
        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        
        Returns:
            Rectangle: The rectangle with the bigger area, or rect_1 if both have the same area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
