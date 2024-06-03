#!/usr/bin/python3
"""This module reads a text file (UTF8)
and prints it to stdout."""

def read_file(filename=""):
    """This function reads a text file UTF8 and prints
    it to stdout"""
    with open(filename, "r", encoding='utf-8') as f:
        print(f.read(), end="")
