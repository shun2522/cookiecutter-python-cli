#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='{{cookiecutter.package_name}}',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click'
    ],
    entry_points={
        'console_scripts': ['{{cookiecutter.command_name}}={{cookiecutter.package_name}}.cli:main']
    }
)
