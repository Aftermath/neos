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

    # list all VMS
    h.list_all_vms
    [<NeosLibvirtVM (stopped): iptables-67b>,
     <NeosLibvirtVM (stopped): katello_foreman>,
     <NeosLibvirtVM (stopped): rhel7.1-yum-keepcache>,
     <NeosLibvirtVM (running): android>]

    # list only stopped vms
    h.list_all_vms
    [<NeosLibvirtVM (stopped): iptables-67b>,
     <NeosLibvirtVM (stopped): katello_foreman>,
     <NeosLibvirtVM (stopped): rhel7.1-yum-keepcache>]

    # list only running vms
    h.list_running_vms
    [<NeosLibvirtVM (running): android>]


    # starting a VM
    vm1 = h.get_vm('iptables-67b')

    # checking vm status
    vm1.status
    'stopped'

    # checking vm name
    vm1.name
    'iptables-67b'

    # starting vm
    vm1.start()
    True

    # checking vm status
    vm1.status
    'running'

