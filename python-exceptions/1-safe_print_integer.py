#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if isinstance(value, int):  # checks if value is an integer
            print("{:d}".format(value))
            return True

    except (TypeError, ValueError):
        return False
