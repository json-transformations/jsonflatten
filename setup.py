from setuptools import setup

setup(
    name='jsonflatten',
    author='Tim Phillips',
    author_email='phillipstr@gmail.com',
    version='0.0',
    url='https://github.com/json-transformations/jsonflatten',
    packages=['jsonflatten'],
    description='A JSON flattening and dataframe generation tool.',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    install_requires=['click', 
                      'jsoncut',
    ],
    extras_require={
        'colors': ['colorama'],
        'json_higlighting': ['pygments']
    },
    entry_points={
        'console_scripts': ['jsonflatten=jsonflatten.cli:main']
    }
)
