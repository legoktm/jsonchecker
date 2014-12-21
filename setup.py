#!/usr/bin/env python3
from setuptools import setup

setup(
    name='jsonchecker',
    version='0.2',
    author='Kunal Mehta',
    author_email='legoktm@gmail.com',
    url='https://github.com/legoktm/jsonchecker/',
    license='Public domain',
    description='A script that validates JSON files and checks for duplicate keys.',
    long_description=open('README.md').read(),
    packages=['jsonchecker'],
    entry_points={
        'console_scripts': [
            'jsonchecker = jsonchecker:main'
        ],
    },
    test_suite='tests.jsonchecker_test',
)
