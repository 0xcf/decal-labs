import lib.util as util


"""
Scenario Overview:
We are going to tank their interface configurations by flushing all addresses
on their interface.  Sadly, thanks to ISC dhclient using raw sockets I can't
use iptables to just firewall off the vagrant/virtualbox DHCP server.

Triage:
Student should use a device reporting command like `ip a` to see that their
device has improper configurations then investigate.  Additionally, they should
notice that I have removed dhcp configuration from their default interface.

Solution:
Student should either manually add the addresses for the interface back to the
device via `ip addr` or even better leave that job up to DHCP by just reloading
the interface.  Sadly I can't tank their DHCP server, so instead they simply
have to just change their interface file back to normal to use the latter
solution.
"""
INTERFACES_FILE = "/etc/network/interfaces"

routing_entries = util.get_default_routing_information()
default_entry = next((e for e in routing_entries if util.is_default_gateway(e)), None)
default_iface = default_entry.iface

# Strip interfaces of configuration
command = "sed -i 's/dhcp/manual/g' {iface_file}".format(iface_file=INTERFACES_FILE)
util.run(command)

# Reload stripped interface
command = "ip addr flush {iface}".format(iface=default_iface)
util.run(command)
