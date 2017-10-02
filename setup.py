import ast
import re
import setuptools
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session=False)
reqs = [str(i.req) for i in install_reqs]

_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('jsonflatten/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()


setuptools.setup(
    name="jsonflatten",
    version=version,
    url="https://github.com/json-transformations/jsonflatten",

    author="Tim Phillips",
    author_email="phillipstr@gmail.com",

    description="A JSON flattening and dataframe generation tool.",
    long_description=readme,

    packages=setuptools.find_packages(),

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],

    install_requires=reqs,

    extras_require={
        'colors': ['colorama'],
        'json_higlighting': ['pygments']
    },

    entry_points={
        'console_scripts': ['jsonflatten='
                            'jsonflatten.cli:main']
    },
)
