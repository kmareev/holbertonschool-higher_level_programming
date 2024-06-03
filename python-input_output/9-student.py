#!/usr/bin/python3
"""Implementation of a function called
'student'"""


class Student:
    """Defines a student with first name, last name
and age."""
    def __init__(self, first_name, last_name, age):
        """Initializes method"""
        self.first_name = first_name
        self.last_name - last_name
        self.age = age

        def to_json(self):
            """Retrieves a dict representation of a Student instance"""
            return self.__dict__
