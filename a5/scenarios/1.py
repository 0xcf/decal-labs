import lib.util as util

"""
Scenario Overview:
Take down the interface that corresponds to their default gateway in the
routing table.  This means they will essentially have no network access
assuming they are relying on this one interface.

Triage:
They should use "ip a" or a similar command to eventually discover that
their interface is downed.  This can be prefaced with an investigation
via ping, traceroute, dig or other realted connectivty tools.

Solution:
Bring the interace back up with "ip link set dev <iface> up"
Note that their routing table may now be missing an entry for a default gateway.
They will have to add this back in based on information they collected
before tanking their system. For example: on my virtual machine I would run
"ip route add default via 10.0.2.2"
"""

command = "ifdown {iface}"
routing_entries = util.get_default_routing_information()
default_entry = next(
    (e for e in routing_entries if util.is_default_gateway(e)),
    None
)

util.run(command.format(iface=default_entry.iface))
