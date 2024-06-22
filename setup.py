# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='movie_loader',
    version='0.1.0',
    description='Downloads and prepares movie data',
    long_description=readme,
    author='Leon Mizera',
    author_email='leon.mizera@stud...',
    url='https://github.com/kennethreitz/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
