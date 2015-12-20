#!/usr/bin/env python
# -*- coding: utf-8  -*-
"""Test jsonchecker."""

import os
import unittest

import jsonchecker


class DuplicateFinderTest(unittest.TestCase):
    """DuplicateFinder base class."""

    def path(self, path):
        """Return test path."""
        return os.path.join(os.path.dirname(__file__), path)

    def check_directory_helper(self, finder, path):
        """Check a directory."""
        finder.check_directory(self.path(path))
        return finder

    def expected_error_helper(self, finder, fname, expected):
        """Assert expected error messages."""
        self.assertIn(self.path(fname), finder.errors)
        self.assertIn(expected, finder.errors[self.path(fname)])


class DuplicateKeyFinderTest(DuplicateFinderTest):
    """Test DuplicateKeyFinder."""

    def setUp(self):
        """Set up."""
        self.finder = jsonchecker.DuplicateKeyFinder()

    def test_check_file(self):
        """Test there are no errors in all known good data files."""
        finder = self.check_directory_helper(self.finder, self.path('testdata/good'))
        self.assertEqual(finder.errors, {})

    def test_check_bad_file(self):
        """Verify errors are detected in all bad data files."""
        finder = self.check_directory_helper(self.finder, self.path('testdata/bad'))
        self.expected_error_helper(finder, 'testdata/bad/bad.json', 'key')
        self.expected_error_helper(finder, 'testdata/bad/bad2.json', 'key3')
        self.expected_error_helper(finder, 'testdata/bad/bad3.json', 'key6')
        self.assertIn(self.path('testdata/bad/invalid.json'), finder.invalids)


class DuplicateValueFinderTest(DuplicateFinderTest):
    """Test DuplicateValueFinder."""

    def setUp(self):
        """Set up."""
        self.finder = jsonchecker.DuplicateValueFinder()

    def test_check_file(self):
        """Test there are no errors in all known good data files."""
        finder = self.check_directory_helper(self.finder, self.path('testdata/good'))
        self.assertEqual(finder.errors, {})

    def test_check_bad_file(self):
        """Verify errors are detected in all bad data files."""
        finder = self.check_directory_helper(self.finder, self.path('testdata/bad'))
        self.expected_error_helper(finder, 'testdata/bad/bad-values.json', 'value3')
        self.expected_error_helper(finder, 'testdata/bad/bad-values2.json', 'value11')
        self.assertIn(self.path('testdata/bad/invalid.json'), finder.invalids)


if __name__ == '__main__':
    unittest.main()
