#!/usr/bin/python3
"""
module for max_integer unittest
"""
import unittest
max_integer = __import__('7-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ok_1(self):
        """
        normal usage
        """
        test = [90, 41, -491, 419]
        returned = max_integer(test)
        self.assertEqual(returned, 419)

    def test_ok_2(self):
        """
        None if function call is empty
        """
        retured = max_integer()
        self.assertEqual(retured, None)

    def test_ok_3(self):
        """
        lists contains big numbers
        """
        test = [-111111111111111111111111, 419, 1000000000000000000000000]
        retured = max_integer(test)
        self.assertEqual(retured, 1000000000000000000000000)

    def test_fail_1(self):
        """
        fail if list contains another list
        """
        test = [90, [], -491, 419]
        with self.assertRaises(TypeError):
            max_integer(test)

    def test_fail_2(self):
        """
        fail if list contains a tuple
        """
        test = [90, (), -491, 419]
        with self.assertRaises(TypeError):
            max_integer(test)

    def test_fail_3(self):
        """
        fail if list contains a dictionary
        """
        test = [90, {}, -491, 419]
        with self.assertRaises(TypeError):
            max_integer(test)

    def test_fail_4(self):
        """
        fail if list contains None
        """
        test = [None, 419, 0]
        with self.assertRaises(TypeError):
            max_integer(test)
