#!/usr/bin/python3
"""In this implementation, the Student class initializes a student
with first_name, last_name, and age, and provides a method
to retrieve its attributes as a dictionary,
optionally filtered by a list of attribute names."""


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

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
with values from json dictionary"""
        for key, value in json.items():
            if key in self.__dict__:
                setattr(self, key, value)
