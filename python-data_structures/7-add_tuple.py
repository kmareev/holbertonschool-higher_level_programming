#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure each tuple has at least 2 elements by appending zeros if necessary
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Create a new tuple by adding the first two elements of each tuple
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
