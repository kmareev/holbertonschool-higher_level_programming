#!/usr/bin/python3
"""This is an empty BaseGeometry class.
"""


class BaseGeometry:
    """An empty class caleld BaseGeomatry."""

    def area(self):
        """Area not implemented."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates the value to ensure it is a positive integer

        Args:
            name (str): The name of the value
            value (int): The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
