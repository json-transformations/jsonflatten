import ast
import re
import sys
from setuptools import setup, find_packages


# get __version__ from __init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('jsonflatten/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

# load README.rst
if sys.version[0] == '3':
    with open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
else:
    with open('README.rst', 'r') as f:
        readme = f.read()


setup(
    name="jsonflatten",
    version=version,
    url="https://github.com/json-transformations/jsonflatten",
    keywords=[],

    author="Tim Phillips",
    author_email="phillipstr@gmail.com",

    description="A JSON flattening and dataframe generation tool.",
    long_description=readme,

    packages=find_packages(include=['jsonflatten']),
    include_package_data=True,
    zipsafe=False,

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],

    install_requires=[
        'jsoncut',
        'click>=6.0',
    ],

    test_suite='tests',
    test_requires=[
        'pytest-cov',
        'flake8',
        'tox',
    ],

    setup_requires=['pytest-runner'],

    entry_points={
        'console_scripts': ['jsonflatten='
                            'jsonflatten.cli:main']
    },
)
