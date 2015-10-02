#!/usr/bin/env python
# -*- coding: utf-8  -*-
"""Script to detect duplicate keys in JSON files."""
from __future__ import print_function

import json
import os
import sys

from collections import defaultdict


class DuplicateKeyFinder(object):

    """Duplicate Key Finder."""

    def __init__(self, quiet=False):
        """Constructor."""
        self.errors = defaultdict(list)
        self.invalids = {}
        self.quiet = quiet

    def mark_error(self, key, fname):
        """Record an error."""
        self.errors[fname].append(key)

    def checker(self, seq, fname):
        """Check routine."""
        d = {}
        for key, value in seq:
            if key in d:
                self.mark_error(key, fname)
            else:
                d[key] = value
        return d

    def check_directory(self, directory):
        """Check one directory."""
        if directory == '.':
            directory = os.getcwd()
        if os.path.isdir(directory):
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
        self.exit()

    def exit(self):
        """print errors and exit."""
        if self.errors or self.invalids:
            if self.quiet:
                print('')
            for fname in self.errors:
                print('----')
                print('Duplicate keys found in %s:' % fname)
                for key in self.errors[fname]:
                    print('* %s' % key)
            for fname, tb in self.invalids.items():
                print('----')
                print('Error while parsing %s:' % fname)
                print(tb)
            return 1
        else:
            if self.quiet:
                print('')
            return 0


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
    sys.exit(finder.run(directories))

if __name__ == '__main__':
    main()
