import lib.util as util


"""
Scenario Overview:
Poison the user's routing table by redirecting traffic
intended for the default gateway to instead go to an invalid IP address.

Triage:
The student should identify the issue by inspecting the machine's arp table
via a tool like "arp".  They should note that the IP address that
corresponds to their default gateway is set to an invalid IP address,
their default interface in this case.

Solution:
Delete the malicious entry and add a proper entry to the gateway's IP address.
They should have taken note of proper configuration info
prior to tanking their system.

The malicious entry should be deleted by using
ip route delete default

A valid entry should be added back using
ip route add default via {gateway-ip}
"""
# Memorize their current default gateway
routing_entries = util.get_default_routing_information()
default_entry = next((e for e in routing_entries if util.is_default_gateway(e)), None)
default_iface_entry = next(
    (e for e in routing_entries if not util.is_default_gateway(e) and e.iface == default_entry.iface),
    None
)

# Kill their default gateway routing rule
command = "ip route delete default"
util.run(command)

# Add a dummy entry
command = "ip route add default via {gateway}".format(
    gateway=util.get_iface_ip_address(default_iface_entry.iface)
)

util.run(command)
