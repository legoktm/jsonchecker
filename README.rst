jsonchecker
===========
.. image:: https://travis-ci.org/legoktm/jsonchecker.svg?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/legoktm/jsonchecker

Checks a JSON file for any duplicate keys, which would be ignored by the normal
parser.

Inspired by and based off of a python-list mailing list post:
<https://mail.python.org/pipermail/python-list/2013-May/660874.html>.

Usage:

* ```jsonchecker file_to_validate.json```

* ```jsonchecker directory/of/json/files/```

An optional --quiet argument can be passed, and will cause the script to print out a . instead
of the full filename for each file scanned. Useful if you plan on checking a large number of files.

The script will exit with a status code of 1 if any duplicate keys are found,
0 if none are.

Released into the public domain.
