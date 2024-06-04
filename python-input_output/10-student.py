#!/usr/bin/python3
"""In this implementation, the __init__ method initializes
the first_name, last_name, and age attributes, and the to_json
method returns a dictionary representation of a Student instance with
these attributes."""


class Student:
    """Defines a student with first name, last name
and age."""
    def __init__(self, first_name, last_name, age):
        """Initializes method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictrionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    json_dict[key] = self.__dict__[key]
            return json_dict
