# coding=utf-8
"""Python Neos setup script."""
from neos.macros import (
    __version__, PROJECT_AUTHOR, PROJECT_CLASSIFIERS, PROJECT_DESCRIPTION,
    PROJECT_EMAIL, PROJECT_KEYWORDS, PROJECT_LICENSE, PROJECT_NAME, PROJECT_URL)

from setuptools import setup

setup(
    name=PROJECT_NAME,
    packages=['neos'],
    version=__version__,
    description=PROJECT_DESCRIPTION,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    url=PROJECT_URL,
    license=PROJECT_LICENSE,
    include_package_data=True,
    install_requires=['libvirt-python'],
    test_suite='tests',
    keywords=PROJECT_KEYWORDS,
    classifiers=PROJECT_CLASSIFIERS,
)
