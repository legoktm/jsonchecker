#!/usr/bin/env python

import json
import os
import sys


def checker(seq):
    d = {}
    for key, value in seq:
        if key in d:
            raise ValueError("Duplicate key %r found" % key)
        else:
            d[key] = value
    return d


def check_directory(directory):
    files = os.listdir(directory)
    for fname in files:
        fname = os.path.join(directory, fname)
        if os.path.isdir(fname) and not fname.startswith('.'):
            check_directory(fname)
            continue
        if not (os.path.isfile(fname) and fname.endswith('.json')):
            continue
        print 'Checking %s...' % fname
        check_file(fname)
    return True


def check_file(fname):
    """
    Check the contents of the given file
    """
    with open(fname) as f:
        text = f.read()
    json.loads(text, object_pairs_hook=checker)
    # No exception was raised
    return True


def main():
    fname = sys.argv[1]
    if os.path.isdir(fname) and check_directory(fname):
        print 'No duplicate keys found'
    elif check_file(fname):
        print 'No duplicate keys found'

if __name__ == '__main__':
    main()
