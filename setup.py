#!/usr/bin/python

from assets.thornet_info import version
from distutils.core import setup


setup(
    name='Thornet Toolset',
    version=str(version),
    scripts=['thornet'],
    packages=['assets'],
    url='https://github.com/5kyc0d3r/thornet',
    license='MIT',
    author='5kyc0d3r',
    author_email='skycoder.official@protonmail.com',
    description='Automated attacks, no more typing in long ass commands.'
)
