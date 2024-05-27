#!/usr/bin/python3

def add_integer(a, b=98):
    """Adds two integers or floats.

        Args:
            a. the first number, must be an int or float.
            b. the second number, must an int or float.
        Returns:
            The sum of a and b as an integer.
        Raises:
            TypeError: if a or b are not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast to integers if they are float

    a = int(a)
    b = int(b)

    return a + b
