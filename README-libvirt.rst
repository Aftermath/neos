Working with Libvirt
--------------------

.. code-block:: python

    from neos.hypervisor.libvirt import NeosHypervisorLibvirt

    # dbus authentication (default)
    h = NeosHypervisorLibvirt()

    h.family
    'QUEMU'

    h.uri
    'qemu:///system'

    # getting a list of all vms
    h.list_all_vms
    ['iptables-67b', 'katello_foreman',
     'rhel7.1-yum-keepcache', 'fedora25', 'android']

    # list with tuple objects from running vms
    [('fedora25', <libvirt.virDomain at 0x7fdc9c068668>),
     ('android', <libvirt.virDomain at 0x7fdc9c0659e8>)]
