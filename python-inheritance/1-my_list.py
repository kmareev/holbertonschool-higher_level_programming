#!/usr/bin/python3
"""This module defines the MyList class, with a functionality
to print the list in ascending order"""

class MyList(list):
    """A subclass of list with an additional method to
    print the list sorted"""

    def print_sorted(self):
        """Prints the list in ascending sorted order"""
        print(sorted(self))
