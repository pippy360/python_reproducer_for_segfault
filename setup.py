#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='lets cause a segfault',
    packages=find_packages(),
    python_requires='>=3.5',
    install_requires=[
        'scikit-learn',
        'hiredis',
        'numpy',
        'redis',
        'scipy',
        'tqdm>=4.29.1',
    ]
)
