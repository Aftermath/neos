# coding: utf-8
# vim:sw=4:ts=4:et:
"""Libvirt Hypervisor file."""
import libvirt
from libvirt import libvirtError

from neos.utils import humanize_bytes
from neos.hypervisor import NeosHypervisor


class NeosHypervisorLibvirt(NeosHypervisor):
    """Define generic class for Libvirt Neos Hypervisor."""

    def __init__(self, uri=None, read_only=False):
        """Init object."""
        super(NeosHypervisorLibvirt, self).__init__()

        self.read_only = bool(read_only)

        if uri is None:
            self.uri = 'qemu:///system'
        else:
            self.uri = uri

        # connect to hypervisor
        self.instance = self.connect()

    def connect(self):
        """Connect to hypervisor and return object."""
        try:
            if self.read_only:
                conn = libvirt.openReadOnly(self.uri)
            else:
                conn = libvirt.open(self.uri)
        except:
            raise
        return conn

    def disconnect(self):
        """Disconnect to hypervisor and return object."""
        if self.is_alive:
            self.instance.close()
        self.instance = None
        return True

    @property
    def get_capabilities(self):
        """Return hypervisor capabilitities."""
        return self.instance.getCapabilities()

    @property
    def get_hostname(self):
        """Return hostname."""
        return self.instance.getHostname()

    @property
    def get_max_vcpus(self):
        """Return max_vcpus."""
        return self.instance.getMaxVcpus(None)

    @property
    def get_cpu_arch(self):
        """Return CPU Arch."""
        return self.instance.getInfo()[0]

    @property
    def get_memory(self):
        """Return Memory Amount."""
        return self.instance.getInfo()[1]

    @property
    def get_cpus(self):
        """Return CPU Count."""
        return self.instance.getInfo()[2]

    @property
    def get_cpu_sockets(self):
        """Return CPU Socket Count."""
        return self.instance.getInfo()[5]

    @property
    def get_cpu_cores_per_socket(self):
        """Return Cores per Socket."""
        return self.instance.getInfo()[6]

    @property
    def get_cpu_threads_per_core(self):
        """Return Threads per Core."""
        return self.instance.getInfo()[7]

    @property
    def family(self):
        """Return OS Family."""
        return self.instance.getType()

    @property
    def is_alive(self):
        """Return Power Status."""
        return bool(self.instance.isAlive())

    @property
    def is_encrypted(self):
        """Return if connection is encyrpted."""
        return bool(self.instance.isEncrypted())

    @property
    def is_secure(self):
        """Return is Secure."""
        return bool(self.instance.isSecure())

    def get_free_memory(self, unit='B'):
        """Return free memory"""
        memory = self.instance.getMemoryStats(
            libvirt.VIR_NODE_MEMORY_STATS_ALL_CELLS)
        return humanize_bytes(memory['free'], unit)

    @property
    def list_all_vms(self):
        """Return a list of all VMS."""
        return self.instance.listDefinedDomains()

    @property
    def list_running_vms(self):
        """List with all running vms (tuple vm name)."""
        vms = []
        for vm_id in self.instance.listDomainsID():
            vm = self.instance.lookupByID(vm_id)
            vms.append((vm.name(), vm))
        return vms

    @property
    def list_nw_filters(self):
        """Return a list of the network filter."""
        return self.instance.listNWFilters()

    def get_vm(self, name):
        """Return VM object if exists."""
        try:
            return self.instance.lookupByName(name)
        except libvirtError as error:
            return error
