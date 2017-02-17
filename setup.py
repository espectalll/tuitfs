#!/usr/bin/env python3
# coding: utf-8

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tuitfs',
    version='0.0.1',

    description='TuitFS client',
    long_description=long_description,

    url='https://github.com/espectalll/tuitfs',

    author='Francisco Gómez García',
    author_email='espectalll@kydara.com',

    license='LGPL',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Database :: Front-Ends',

        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6',
    ],

    keywords='tuitfs twitter database storage awful_life_choices',

    py_modules=["tuitfs"],

    install_requires=['twitter', 'pygobject', 'pyyaml'],

    packages=find_packages(),
    package_dir = {'': 'tuitfs'},
    include_package_data=True,

    data_files=[('tuitfs', ['tuitfs/ui.glade'])],

    entry_points={
        'console_scripts': [
            'tuitfs=tuitfs:main',
        ],
    },
)

