import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

NAME = 'weakCrypt'
DESCRIPTION = 'Fundamentally insecure crypto-explorations.'
URL = 'https://www.github.com/suddensleep/weakCrypt'
EMAIL = 'suddensleep@gmail.com'
AUTHOR = 'John Gilling'
REQUIRES_PYTHON = '>=3.5.0'
VERSION = None

REQUIRED = [
    'numpy'
]

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about('__version__'] = VERSION

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'Topic :: Scientific/Engineering :: Mathematics'
    ]
)
