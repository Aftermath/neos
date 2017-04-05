# coding: utf-8
# vim:sw=4:ts=4:et:
"""Libvirt Hypervisor file."""
import libvirt

from neos.hypervisor import NeosHypervisor


class NeosHypervisorLibvirt(NeosHypervisor):
    """Define generic class for Libvirt Neos Hypervisor."""

    def __init__(self, name, read_only=False):
        """Init object."""
        super(NeosHypervisorLibvirt, self).__init__()
        self.name = name
        self.family = 'libvirt'

        if read_only:
            self.instance = libvirt.openReadOnly(None)
        else:
            self.instance = libvirt.open(None)
