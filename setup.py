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
