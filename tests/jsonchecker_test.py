#!/usr/bin/env python

import os
import unittest

import jsonchecker


class DuplicateKeyFinderTest(unittest.TestCase):

    def path(self, path):
        return os.path.join(os.path.dirname(__file__), path)

    def check_directory_helper(self, path):
        finder = jsonchecker.DuplicateKeyFinder(self.path(path))
        finder.check_directory(self.path(path))
        return finder

    def test_check_file(self):
        finder = self.check_directory_helper(self.path('testdata/good'))
        self.assertEqual(finder.errors, {})

    def test_check_bad_file(self):
        finder = self.check_directory_helper(self.path('testdata/bad'))
        self.assertIn(self.path('testdata/bad/bad.json'), finder.errors)
        self.assertIn('key', finder.errors[self.path('testdata/bad/bad.json')])
        self.assertIn(self.path('testdata/bad/bad2.json'), finder.errors)
        self.assertIn('key3', finder.errors[self.path('testdata/bad/bad2.json')])
        self.assertIn(self.path('testdata/bad/invalid.json'), finder.invalids)


if __name__ == '__main__':
    unittest.main()
