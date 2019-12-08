# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='A simple OCR application',
    version='0.0.1',
    description='',
    long_description=readme,
    author='Aziz Unsal',
    author_email='unsal.aziz@gmail.com',
    packages=find_packages
)
