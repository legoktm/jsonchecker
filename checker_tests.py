#!/usr/bin/env python

import unittest

import checker


class DuplicateKeyFinderTest(unittest.TestCase):
    def check_directory_helper(self, path):
        finder = checker.DuplicateKeyFinder(path)
        finder.check_directory(path)
        return finder

    def test_check_file(self):
        finder = self.check_directory_helper('testdata/good')
        self.assertEqual(finder.errors, {})

    def test_check_bad_file(self):
        finder = self.check_directory_helper('testdata/bad')
        self.assertIn('testdata/bad/bad.json', finder.errors)
        self.assertIn('key', finder.errors['testdata/bad/bad.json'])
        self.assertIn('testdata/bad/bad2.json', finder.errors)
        self.assertIn('key3', finder.errors['testdata/bad/bad2.json'])


if __name__ == '__main__':
    unittest.main()
