#!/usr/bin/python3
"""Unittests for max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer


def one_element_list(self):
    """list with a single element."""
    one_element = [5]
    self.assertEqual(max_integer(one_element), 7)

if __name__ == '__main__':
    unittest.main()
