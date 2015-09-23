from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-context-variables',
    version='0.0.3',
    author='Carl M. Johnson',
    packages=['context_variables'],
    url='https://github.com/carlmjohnson/django-context-variables',
    license='MIT',
    description="Simple utility to help make declarative class-based views in Django",
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
)

