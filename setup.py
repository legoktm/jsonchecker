#!/usr/bin/env python3
# -*- coding: utf-8  -*-
"""Setup jsonchecker."""
from setuptools import setup

setup(
    name='jsonchecker',
    version='0.7.0',
    author='Kunal Mehta',
    author_email='legoktm@gmail.com',
    url='https://github.com/legoktm/jsonchecker/',
    license='Public domain',
    description='A script that validates JSON files and checks for duplicate keys.',
    long_description=open('README.rst').read(),
    packages=['jsonchecker'],
    entry_points={
        'console_scripts': [
            'jsonchecker = jsonchecker:main'
        ],
    },
    test_suite='tests.jsonchecker_test',
)
