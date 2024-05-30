#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_all_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_one_element(self):
        self.assertEqual(max_integer([3]), 3)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_no_argument(self):
        self.assertEqual(max_integer(), None)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([1, -2, 3, -4, 0]), 3)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([1, 3, 3, 2]), 3)

    def test_list_with_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_list_with_ints_and_floats(self):
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)

    def test_large_numbers(self):
        self.assertEqual(max_integer([999999999, 222222222, 333333333]), 999999999)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            max_integer("hello")

    def test_list_of_strings(self):
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])

    def test_list_of_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3])

if __name__ == '__main__':
    unittest.main()