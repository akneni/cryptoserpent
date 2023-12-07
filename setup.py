from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pycrypt',
    version='0.0.1',
    description='A python library for encryption',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Anish Kanthamneni',
    author_email='akneni@gmail.com',
    packages=['pycrypt'],
    install_requires=[
        'numpy',
    ],
)