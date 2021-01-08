#!/usr/bin/python3
"""Unittests for max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer"""
    def test_max_begginning(self):
        """list with beginning max value."""
        max_beginning = [9, 8, 7, 6]
        self.assertEqual(max_integer(max_at_beginning), 9)

    def one_element_list(self):
        """list with a single element."""
        one_element = [5]
        self.assertEqual(max_integer(one_element), 7)

if __name__ == '__main__':
    unittest.main()
