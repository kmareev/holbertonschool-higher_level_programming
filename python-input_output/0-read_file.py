#!/usr/bin/python3
"""This module reads a text file (UTF*)
and prints it to stdout."""

def read_file(filename=""):
    with open(filename, "r", encoding='utf-8') as f:
        print(file.read(), end="")
