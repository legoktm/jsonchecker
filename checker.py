#!/usr/bin/env python

import json
import os
import sys


class DuplicateKeyException(Exception):
    def __init__(self, key):
        self.key = key


def checker(seq):
    d = {}
    for key, value in seq:
        if key in d:
            raise DuplicateKeyException(key)
        else:
            d[key] = value
    return d


def check_directory(directory):
    has_errors = False
    files = os.listdir(directory)
    for fname in files:
        if fname.startswith('.'):
            continue
        fname = os.path.join(directory, fname)
        if os.path.isdir(fname):
            has_errors = check_directory(fname) or has_errors
            continue
        if not (os.path.isfile(fname) and fname.endswith('.json')):
            continue
        print 'Checking %s...' % fname
        try:
            check_file(fname)
        except DuplicateKeyException, e:
            print 'ERROR: Duplicate key found for "%s"' % e.key
            has_errors = True
    return has_errors


def check_file(fname):
    """
    Check the contents of the given file
    """
    with open(fname) as f:
        text = f.read()
    json.loads(text, object_pairs_hook=checker)
    # No errors!
    return False


def main():
    fname = sys.argv[1]
    if os.path.isdir(fname):
        if check_directory(fname):
            # Errors found
            print 'Duplicate keys found.'
            sys.exit(1)
        else:
            print 'No duplicate keys found'
            sys.exit(0)
    else:
        check_file(fname)
        print 'No duplicate keys found'

if __name__ == '__main__':
    main()
