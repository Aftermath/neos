# coding: utf-8
# vim:sw=4:ts=4:et:
"""Neos macros."""
MAJOR_VERSION = 0
MINOR_VERSION = 0
RELEASE_VERSION = 1
__version__ = '{}.{}.{}'.format(MAJOR_VERSION, MINOR_VERSION, RELEASE_VERSION)

PROJECT_AUTHOR = 'Neos Authors'
PROJECT_EMAIL = 'define@example.com'
PROJECT_DESCRIPTION = ('A python-based controller for virtualization '
                       'backends providing a bridge with web-based controls.')
PROJECT_NAME = 'Neos'
PROJECT_LICENSE = 'LGPLv3+'
PROJECT_URL = 'https://github.com/Aftermath/neos'
PROJECT_KEYWORDS = [
    'libvirt', 'virtual machines', 'virtualization', 'kvm'
]

PROJECT_CLASSIFIERS = [
    'Environment :: Other Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: ' +
    'GNU Lesser General Public License v3 or later (LGPLv3+)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]
