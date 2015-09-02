from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-context-variables',
    version='0.0.2',
    author='Carl M. Johnson',
    packages=['context_variables'],
    url='https://github.com/carlmjohnson/django-context-variables',
    license='MIT',
    description='Simple utility to help make declarative class-based views in Django',
    long_description=read('README.md'),
    data_files=[('', ['LICENSE', 'README.md'])]
)
