#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([10, 20, 30]), 30)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -2]), -1)
        self.assertEqual(max_integer([-10, -20, -30]), -10)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 0, 10]), 10)
        self.assertEqual(max_integer([-10, 10, 0]), 10)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_large_list(self):
        self.assertEqual(max_integer(list(range(1000000))), 999999)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5]), -1.5)


if __name__ == '__main__':
    unittest.main()
