#!/usr/bin/env python3
# -*- coding: utf-8  -*-
"""Setup jsonchecker."""
from setuptools import setup

init_py = open('jsonchecker/__init__.py').read().splitlines()
metadata = [('__doc__', line) if line.startswith('"""')
            else line.split(' = ')
            for line in init_py
            if line.startswith('__') or line.startswith('"""')]
metadata = dict((name[2:-2], value.strip('"\'')) for name, value in metadata)

setup(
    name='jsonchecker',
    version=metadata['version'],
    author=metadata['author'],
    author_email=metadata['email'],
    url=metadata['url'],
    license='Public domain',
    description=metadata['doc'],
    long_description=open('README.rst').read(),
    packages=['jsonchecker'],
    entry_points={
        'console_scripts': [
            'jsonchecker = jsonchecker:main'
        ],
    },
    test_suite='tests.jsonchecker_test',
    classifiers=[
        'License :: Public Domain',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: Jython',
        'Programming Language :: Python :: Implementation :: Stackless',
    ],
)
