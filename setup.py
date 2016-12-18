# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='hpds',
    version='0.0.1',
    description='High performance data structures in python.',
    long_description=readme,
    author='David Skoda',
    author_email='dskoda1@binghamton.edu',
    url='https://github.com/dskoda/hpds',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
