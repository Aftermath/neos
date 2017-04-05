# coding: utf-8
# vim:sw=4:ts=4:et:
"""Init Hypervisor file."""


class NeosHypervisor(object):
    """Define generic class for Neos Hypervisor."""

    def __init__(self):
        """Init NeosHypervisor class."""
        pass

    def connect(self):
        """Connect to a hypervisor."""
        pass

    def create_snapshot(self):
        """Create Snapshot."""
        pass

    def list_vms(self):
        """List virtual machine."""
        pass

    def remove_snapshot(self):
        """Remove Snapshot."""
        pass

    def start_vm(self):
        """Start virtual machine."""
        pass

    def stop_vm(self):
        """Stop virtual machine."""
        pass
