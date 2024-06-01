#!/usr/bin/python3
"""This module created an abstract class named Shape,
using the ABC package."""


from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract class called Shape."""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """This is a subclass of Shape representing
    Circle."""

    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return math.pi * self.radius ** 2

    def  perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """This is a subclass of Shape representing
    a Rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
