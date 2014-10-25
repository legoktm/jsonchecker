#!/usr/bin/env python

import json
import sys


def checker(seq):
    d = {}
    for key, value in seq:
        if key in d:
            raise ValueError("Duplicate key %r found" % key)
        else:
            d[key] = value
    return d


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
    if check_file(fname):
        print 'No duplicate keys found'

if __name__ == '__main__':
    main()
