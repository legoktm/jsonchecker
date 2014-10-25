#!/usr/bin/env python

import unittest

import checker


class CheckerTest(unittest.TestCase):
    def test_check_file(self):
        self.assertTrue(checker.check_file('good.json'))
        self.assertRaises(ValueError, checker.check_file, 'bad.json')

if __name__ == '__main__':
    unittest.main()
