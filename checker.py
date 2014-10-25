#!/usr/bin/env python
from __future__ import print_function

from collections import defaultdict
import json
import os
import sys


class DuplicateKeyFinder:
    def __init__(self, directory):
        self.directory = directory
        self.errors = defaultdict(list)
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
        files = os.listdir(directory)
        for fname in files:
            if fname.startswith('.'):
                continue
            fname = os.path.join(directory, fname)
            if os.path.isdir(fname):
                has_errors = self.check_directory(fname) or has_errors
                continue
            if not (os.path.isfile(fname) and fname.endswith('.json')):
                continue
            print('Checking %s...' % fname)
            self.current_fname = fname
            self.check_file(fname)

    def check_file(self, fname):
        """
        Check the contents of the given file
        """
        with open(fname) as f:
            text = f.read()
        json.loads(text, object_pairs_hook=self.checker)

    def run(self):
        self.check_directory(self.directory)
        self.exit()

    def exit(self):
        if self.errors:
            for fname in self.errors:
                print('----')
                print('Duplicate keys found in %s:' % fname)
                for key in self.errors[fname]:
                    print('* %s' % key)
            sys.exit(1)
        else:
            sys.exit(0)


if __name__ == '__main__':
    finder = DuplicateKeyFinder(sys.argv[1])
    finder.run()
