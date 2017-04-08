# coding: utf-8
# vim:sw=4:ts=4:et:
"""Init Hypervisor file."""


class NeosHypervisor(object):
    """Define generic class for Neos Hypervisor."""

    def __init__(self, name='localhost'):
        """Init NeosHypervisor class."""
        self.uri = None
        return None

    def __repr__(self):
        """Object representation."""
        return "<{0}: {1}>".format(self.__class__.__name__, self.uri)
