#!/usr/bin/env python3
"""This module is a basic serialization module that
adds the functionality to serialize a Python dictionary to a 
JSON file and deserialize the JSON file to recreate the Python Dictionary"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data: A Python dictionary with data.
        filename: The filename of the output JSON file.
                  If the output file already exists it should be replaced.
    """
    try:
        with open(filename, "w", encoding="utf-8") as jfile:
            json.dump(data, jfile)
    except Exception as e:
        print(f"An error occurred while saving to file: {e}")


def load_and_deserialize(filename):
    """
    Deserialize the JSON file to recreate the Python dictionary.

    Args:
        filename: The filename of the input JSON file.

    Returns:
        A Python dictionary with the deserialized JSON data from the file.
    """
    try:
        with open(filename, "r", encoding="utf-8") as pyfile:
            return json.load(pyfile)
    except Exception as e:
        print(f"An error occurred while loading from file: {e}")
        return None
