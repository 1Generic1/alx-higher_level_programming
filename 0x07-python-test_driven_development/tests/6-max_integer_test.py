#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Test for each cases """
    def test_max_integer_positive_values(self):
        result = max_integer([1, 3, 5, 2, 4])
        self.assertEqual(result, 5)

    def test_max_integer_negative_values(self):
        result = max_integer([-10, -5, -8, -15])
        self.assertEqual(result, -5)

    def test_max_integer_mixed_values(self):
        result = max_integer([-2, 0, 7, -1, 10])
        self.assertEqual(result, 10)

    def test_max_integer_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer_single_value(self):
        result = max_integer([42])
        self.assertEqual(result, 42)

if __name__ == '__main__':
    unittest.main()
