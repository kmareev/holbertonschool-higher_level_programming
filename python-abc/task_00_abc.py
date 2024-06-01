#!/usr/bin/python3
"""This module creates an abstract class of Animal,
using the ABC module."""

from abc import ABC, abstractmethod

class Animal(ABC):
    """abstract class Animal"""
    @abstractmethod
    def sound(self):
        """abstract method sound"""
        pass

class Dog(Animal):
    """subclass of Animal representing a Dog"""
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    """subclass of Animal representing a Cat"""
    def sound(self):
        return "Meow"
