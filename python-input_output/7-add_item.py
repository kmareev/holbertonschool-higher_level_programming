#!/usr/bin/python3
"""This module writes a script that adds all arguments to
a Python list, and then saves them to a file add_items.json.

It uses the functions save_to_json_file and load_from_json_file
for handling JSON data."""


import sys
import os


# Constants
FILENAME = "add_item.json"

# Import the functions from the respective files
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def main():
    """Main function to add command-line arguments to the list and save them."""
    # Load existing items if the file exists, otherwise create an empty list
    if os.path.exists(FILENAME):
        items = load_from_json_file(FILENAME)
    else:
        items = []

    # Add all command-line arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(items, FILENAME)
