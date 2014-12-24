#!/usr/bin/env python
from __future__ import print_function

from collections import defaultdict
import json
import os
import sys


class DuplicateKeyFinder:
    def __init__(self, quiet=False):
        self.errors = defaultdict(list)
        self.invalids = {}
        self.quiet = quiet
        self.current_fname = None

    def mark_error(self, key):
        if self.current_fname:
            self.errors[self.current_fname].append(key)

    def checker(self, seq):
        d = {}
        for key, value in seq:
            if key in d:
                self.mark_error(key)
            else:
                d[key] = value
        return d

    def check_directory(self, directory):
        has_errors = False
        if os.path.isdir(directory):
            files = [os.path.join(directory, fname) for fname in os.listdir(directory)]
        else:
            files = [directory]
        for fname in files:
            if fname.startswith('.'):
                continue
            if os.path.isdir(fname):
                has_errors = self.check_directory(fname) or has_errors
                continue
            if not (os.path.isfile(fname) and fname.endswith('.json')):
                continue
            if self.quiet:
                print('.', end='')
            else:
                print('Checking %s...' % fname)
            self.current_fname = fname
            self.check_file(fname)

    def check_file(self, fname):
        """
        Check the contents of the given file
        """
        with open(fname) as f:
            text = f.read()
        try:
            json.loads(text, object_pairs_hook=self.checker)
        except ValueError as e:
            self.invalids[fname] = str(e)

    def run(self, directories):
        for directory in directories:
            self.check_directory(directory)
        self.exit()

    def exit(self):
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
            sys.exit(1)
        else:
            if self.quiet:
                print('')
            sys.exit(0)


def main():
    finder = DuplicateKeyFinder(quiet='--quiet' in sys.argv)
    directories = []
    for arg in sys.argv[1:]:
        if not arg.startswith('--'):
            directories.append(arg)
    if not directories:
        print('No files or directories provided')
        sys.exit(1)
    finder.run(directories)

if __name__ == '__main__':
    main()
