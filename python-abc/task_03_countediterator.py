#!/usr/bin/python3
"""This module uses a built-in iterator 'iter' function."""

class CountedIterator:
    """A custom iterator that extends the functionality
    of a standard iterator to count the number of items
    iterator over."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        """Returns the next item from the iterator and
        increments the counter.
        Raises:
            StopIteration: If there are no more items
            in the iterator."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
        
    def get_count(self):
        """Returns the number of items that have been iterator over."""
        return self.counter
