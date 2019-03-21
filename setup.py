#!/usr/bin/env python3

"""Setup for look4bas"""
from setuptools import find_packages, setup

setup(
    name='look4bas',
    description="Search for Gaussian basis sets",
    long_description='Command line tool to search for contracted Gaussian-type basis '
    'sets in electronic structure theory',
    #
    url='https://github.com/mfherbst/look4bas',
    author='Michael F. Herbst',
    author_email="info@michael-herbst.com",
    license="GPL v3",
    #
    packages=find_packages(exclude=["*.test*", "test"]),
    scripts=["bin/look4bas"],
    version='0.3.0',
    #
    python_requires='>=3.5',
    install_requires=[
        'requests (>=2.2)',
        'beautifulsoup4 (>= 4.2)',
        'lxml (>= 4.2)'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Science/Research',
        "Topic :: Scientific/Engineering :: Chemistry",
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: Unix',
    ],
)
