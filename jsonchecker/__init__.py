#!/usr/bin/env python
# -*- coding: utf-8  -*-
"""Script that validates JSON files and checks for duplicate keys."""
from __future__ import print_function

import json
import os
import sys

from collections import defaultdict

__url__ = 'https://github.com/legoktm/jsonchecker'
__author__ = 'Kunal Mehta'
__email__ = 'legoktm@member.fsf.org'
__version__ = '0.8.0'


class DuplicateFinder(object):
    """Duplicate Finder base class."""

    def __init__(self, quiet=False):
        """Constructor."""
        self.errors = defaultdict(list)
        self.invalids = {}
        self.quiet = quiet

    def mark_error(self, key, fname):
        """Record an error."""
        self.errors[fname].append(key)

    def check_directory(self, directory):
        """Check one directory."""
        directory = os.path.abspath(directory)
        if os.path.isdir(directory):
            last_directory = os.path.basename(directory)
            if last_directory.startswith("."):
                return
            files = [os.path.join(directory, fname) for fname in os.listdir(directory)]
        else:
            files = [directory]
        for fname in files:
            if fname.startswith('.'):
                continue
            if os.path.isdir(fname):
                self.check_directory(fname)
                continue
            if not (os.path.isfile(fname) and fname.endswith('.json')):
                continue
            if self.quiet:
                print('.', end='')
            else:
                print('Checking %s...' % fname)
            self.check_file(fname)

    def check_file(self, fname):
        """Check the contents of the given file."""
        with open(fname) as f:
            text = f.read()
        try:
            json.loads(text, object_pairs_hook=lambda seq: self.checker(seq, fname))
        except ValueError as e:
            self.invalids[fname] = str(e)

    def run(self, directories):
        """Check each directory in directories."""
        for directory in directories:
            self.check_directory(directory)
        return self.exit()

    def exit_with_msg(self, msg):
        """print errors and exit."""
        if self.errors or self.invalids:
            if self.quiet:
                print('')
            for fname in self.errors:
                print('----')
                print('Duplicate %s found in %s:' % (msg, fname))
                for duplicate in self.errors[fname]:
                    print('* %s' % duplicate)
            for fname, tb in self.invalids.items():
                print('----')
                print('Error while parsing %s:' % fname)
                print(tb)
            return 1
        else:
            if self.quiet:
                print('')
            return 0


class DuplicateKeyFinder(DuplicateFinder):
    """Duplicate Key Finder."""

    def checker(self, seq, fname):
        """Check routine."""
        d = {}
        for key, value in seq:
            if key in d:
                self.mark_error(key, fname)
            else:
                d[key] = value
        return d

    def exit(self):
        """print errors and exit."""
        return self.exit_with_msg('keys')


class DuplicateValueFinder(DuplicateFinder):
    """Duplicate Value Finder."""

    def hashable(self, v):
        """Determine whether `v` can be hashed."""
        try:
            hash(v)
        except TypeError:
            return False
        return True

    def dupes_in_list(self, l):
        """Return hashable duplicates from this list."""
        seen = set()
        seen_twice = set()
        # Adds all elements it doesn't know yet to seen and
        # adds all others to seen_twice
        for x in l:
            if self.hashable(x):
                if x in seen:
                    seen_twice.add(x)
                else:
                    seen.add(x)
        return list(seen_twice)

    def checker(self, seq, fname):
        """Check routine."""
        d = {}
        for key, value in seq:
            if isinstance(value, list):
                dupes = self.dupes_in_list(value)
                good = []
                for x in value:
                    if x in dupes and x not in self.errors[fname]:
                        self.mark_error(x, fname)
                    else:
                        good.append(x)
                d[key] = good
            else:
                d[key] = value
        return d

    def exit(self):
        """print errors and exit."""
        return self.exit_with_msg('values')


def main():
    """Main entry point."""
    finder = DuplicateKeyFinder(quiet='--quiet' in sys.argv)
    directories = []
    for arg in sys.argv[1:]:
        if not arg.startswith('--'):
            directories.append(arg)
    if not directories:
        print('No files or directories provided')
        sys.exit(1)
    ret = finder.run(directories)

    if '--values' in sys.argv:
        finder = DuplicateValueFinder(quiet='--quiet' in sys.argv)
        ret = finder.run(directories) | ret

    sys.exit(ret)

if __name__ == '__main__':
    main()
