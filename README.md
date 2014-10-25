dupe-keys-json
====
[![Build Status](https://travis-ci.org/legoktm/dupe-keys-json.svg?branch=master)](https://travis-ci.org/legoktm/dupe-keys-json)

Checks a JSON file for any duplicate keys, which would be ignored by the normal
parser.

Inspired by and based off of:
<https://mail.python.org/pipermail/python-list/2013-May/647954.html>.

Usage:

* ```python checker.py file_to_validate.json```

* ```python checker.py directory/of/json/files/```

The script will exit with a status code of 1 if any duplicate keys are found,
0 if none are.

Released into the public domain.
