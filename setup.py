#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'six>=1.5.2',
    'filelock>=2.0'
]

setup(
    name='forklift',
    version='0.0.1',
    description="Download support data for Python pacakges, like sample data for tests and binary databases.",
    long_description=readme + '\n\n' + history,
    author="Guilherme Castelão",
    author_email='guilherme@castelao.net',
    url='https://github.com/castelao/forklift',
    packages=[
        'forklift',
    ],
    package_dir={'forklift':
                 'forklift'},
    },
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='forklift',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ]
)