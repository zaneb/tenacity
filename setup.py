#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

settings = dict()


# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

settings.update(
    name='retrying',
    version='1.0.0',
    description='Retry any arbitrary function conditionally via a decorator',
    long_description=open('README.rst').read(),
    author='Ray Holder',
    url='https://github.com/rholder/retrying',
    keywords="context manager decorator decorators retry retrying exception exponential backoff",
    py_modules= ['retrying'],
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    )
)


setup(**settings)
