#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


# extensions
entry_points = {
    'pygments.styles': [
        'topas=topas_pygments:TopasStyle',
    ],
    'pygments.lexers': [
        'topas=topas_pygments:TopasLexer',
        'plain=topas_pygments:PlainLexer',
    ],
}

setup(
    name='topas-pygments',
    version='0.2.0',
    description="TOPAS plugins for pygments",
    author="David Hall",
    author_email='dhcrawley@gmail.com',
    url='https://github.com/davidchall/topas-pygments',
    packages=[
        'topas_pygments',
    ],
    entry_points=entry_points,
    include_package_data=True,
    install_requires=[
        'pygments',
    ]
)
