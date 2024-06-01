#!/usr/bin/python3
"""This module uses multiple inheritance."""

class Fish:
    """A class representing a Fish"""
    def swim(self):
        print("The fish is swimming")
    def habitat(self):
        print("The fish lives in water")
    
class Bird:
    """A class representing a Bird"""
    def fly(self):
        print("The bird is flying")
    def habitat(self):
        print("The bird lives in the sky")
    
class FlyingFish(Fish, Bird):
    """A class representing a FlyingFish,
    inheriting from Fish and Bird, known as multiple
    inheritance."""

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
    