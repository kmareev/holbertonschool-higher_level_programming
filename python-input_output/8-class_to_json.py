#!/usr/bin/python3
"""The implementation of a function
'class_to_json."""


def class_to_json(obj):
    """Returns a dictionary description with simple data structure
for JSON serialization of an object"""
    return obj.__dict__
