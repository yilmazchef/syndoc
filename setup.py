# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='SynDoc',
    version='0.0.1',
    description='Python package to auto-generate pdf, docx, pptx, odt, html from md (markdown) files.',
    long_description=readme,
    author='Yilmaz Mustafa',
    author_email='yilmaz_mustafa@outlook.be',
    url='https://github.com/yilmazchef/syndoc',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
