import lib.util as util


routing_entries = util.get_default_routing_information()
default_entry = next((e for e in routing_entries if util.is_default_gateway(e)), None)
default_iface_entry = next(
    (e for e in routing_entries if not util.is_default_gateway(e) and e.iface == default_entry.iface),
    None
)

command = "ip route delete default"
util.run(command)

command = "ip route add default via {gateway}".format(
    gateway=util.get_iface_ip_address(default_iface_entry.iface)
)

util.run(command)
