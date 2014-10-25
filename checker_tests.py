#!/usr/bin/env python

import unittest

import checker


class CheckerTest(unittest.TestCase):
    def test_check_file_good(self):
        self.assertFalse(checker.check_file('good.json'))

    def test_check_file_bad(self):
        self.assertRaises(
            checker.DuplicateKeyException,
            checker.check_file,
            'bad.json'
        )

if __name__ == '__main__':
    unittest.main()
