#!/usr/bin/env python

from setuptools import setup, find_packages


PACKAGE = 'bitcointabunspent'

setup(
    name=PACKAGE,
    description='Tabulate listunspent to show balance per address.',
    version='0.1',
    author='Nathan Wilcox',
    author_email='nejucomo@gmail.com',
    license='GPLv3',
    url='https://github.com/nejucomo/{}'.format(PACKAGE),

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            '{} = {}.main:main'.format(
                PACKAGE.replace('_', '-'),
                PACKAGE,
            )
        ],
    }
)
