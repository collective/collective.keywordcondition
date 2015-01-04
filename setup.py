# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.1.dev0'

long_description = (
    read('README.rst')
    + '\n' +
    read('docs/HISTORY.rst')
    + '\n' +
    read('CONTRIBUTORS.rst')
    )

setup(
    name='collective.keywordcondition',
    version=version,
    description="A condition for Plone 3's content rules that checks keywords on a content item",
    long_description=long_description,

    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords='Plone content rules',
    author='Martin Aspeli',
    author_email='optilude@gmail.com',
    url='https://github.com/collective/collective.keywordcondition',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        ],

    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
        },
    )
