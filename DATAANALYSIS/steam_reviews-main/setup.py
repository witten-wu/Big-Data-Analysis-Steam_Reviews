# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='steam_reviews',
    version='0.1.0',
    description='analyzing reviews of users in Steam',
    long_description=readme,
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)